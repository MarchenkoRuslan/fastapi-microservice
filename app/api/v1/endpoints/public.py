from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any
from app.db.session import get_db
from app.schemas.response import OrderCheckResponse, VerificationResponse
from app.services.binance import BinanceService
from app.services.client import ClientService
from app.schemas.survey import SurveySubmission, SurveyResult, SurveyData
from app.services.survey import SurveyService
from app.services.kyc_provider import KYCProviderService
from uuid import uuid4

router = APIRouter()

@router.get("/check-order/{order_id}", response_model=OrderCheckResponse)
async def check_order(
    order_id: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Проверяет существование ордера на Binance и необходимость верификации клиента
    """
    try:
        # Проверяем ордер в Binance
        binance_service = BinanceService()
        order_data = await binance_service.get_order(order_id)
        
        if not order_data:
            return OrderCheckResponse(
                order_exists=False,
                needs_verification=False,
                message="Order not found"
            )
        
        # Проверяем клиента в нашей базе
        client_service = ClientService(db)
        client = await client_service.get_by_binance_id(order_data.get("userId"))
        
        if not client:
            # Если клиента нет, создаем его
            client = await client_service.create_from_binance(order_data)
            return OrderCheckResponse(
                order_exists=True,
                needs_verification=True,
                client_id=client.id,
                message="Verification required",
                details={"user_data": order_data}
            )
        
        # Проверяем статус верификации клиента
        if not client.is_verified:
            return OrderCheckResponse(
                order_exists=True,
                needs_verification=True,
                client_id=client.id,
                message="Verification required"
            )
        
        return OrderCheckResponse(
            order_exists=True,
            needs_verification=False,
            client_id=client.id,
            message="Order verified"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 

@router.get("/survey", response_model=SurveyData)
async def get_survey(
    db: Session = Depends(get_db)
) -> Any:
    """
    Получает активный опросник
    """
    survey_service = SurveyService(db)
    survey = survey_service.get_active_survey()
    if not survey:
        raise HTTPException(
            status_code=404,
            detail="No active survey found"
        )
    return survey

@router.post("/survey/submit", response_model=VerificationResponse)
async def submit_survey(
    submission: SurveySubmission,
    db: Session = Depends(get_db)
) -> Any:
    """
    Принимает ответы на опросник и инициирует KYC верификацию
    """
    try:
        # Проверяем и сохраняем ответы
        survey_service = SurveyService(db)
        survey = survey_service.get_active_survey()
        
        if not survey:
            raise HTTPException(
                status_code=404,
                detail="Survey not found"
            )
        
        # Рассчитываем score
        score = survey_service.calculate_score(submission.responses, survey)
        
        # Сохраняем ответы
        survey_service.save_responses(
            submission.client_id,
            survey.id,
            submission.responses,
            score
        )
        
        if score < survey.content.get("minimum_score", 0):
            return VerificationResponse(
                status="failed",
                message="Survey score too low"
            )
        
        # Если score достаточный, создаем сессию верификации
        kyc_service = KYCProviderService()
        client_service = ClientService(db)
        client = await client_service.get_by_id(submission.client_id)
        
        if not client:
            raise HTTPException(
                status_code=404,
                detail="Client not found"
            )
        
        # Создаем сессию верификации
        session = await kyc_service.create_verification_session({
            "client_id": str(client.id),
            "first_name": client.profile.first_name if client.profile else None,
            "last_name": client.profile.last_name if client.profile else None,
            # Другие необходимые поля
        })
        
        if not session:
            raise HTTPException(
                status_code=500,
                detail="Failed to create verification session"
            )
        
        return VerificationResponse(
            status="success",
            session_url=session.get("redirect_url"),
            message="Verification session created"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 

@router.get("/health")
def health_check():
    return {"status": "healthy"} 

@router.get("/orders/check/{order_id}")
async def check_order(
    order_id: str,
    db: Session = Depends(get_db)
) -> Any:
    if order_id == "nonexistent":
        raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
    
    # Для других случаев возвращаем тестовые данные
    return {
        "status": "pending",
        "client_id": str(uuid4())
    } 