from fastapi import APIRouter, Depends
from typing import Any
from sqlalchemy.orm import Session
from app.schemas.response import ResponseModel
from app.schemas.binance import OrderCheckRequest
from app.services.binance import BinanceService
from app.db.session import get_db

router = APIRouter()


@router.post(
    "/checkOrder",
    response_model=ResponseModel,
    summary="Проверка P2P ордера Binance",
    description="""
    Проверяет существование ордера в Binance P2P и возвращает информацию о продавце.
    
    Пример запроса:
    ```json
    {
        "order_number": "123456789"
    }
    ```
    
    Пример успешного ответа:
    ```json
    {
        "status": "success",
        "data": {
            "orderNumber": "123456789",
            "sellerName": "John Doe",
            "sellerNickname": "johndoe",
            "sellerMobilePhone": "+1234567890",
            "status": "COMPLETED"
        }
    }
    """
)
async def check_order(
    request: OrderCheckRequest,
    db: Session = Depends(get_db)
) -> Any:
    """
    Проверяет существование ордера в Binance P2P.
    
    Args:
        request: OrderCheckRequest с номером ордера
    
    Returns:
        ResponseModel с информацией об ордере и продавце
    """
    try:
        binance_service = BinanceService()
        order_data = await binance_service.get_user_order_detail(request.order_number)
        
        return ResponseModel(
            status="success",
            data=order_data
        )
    except Exception as e:
        return ResponseModel(
            status="error",
            message=str(e)
        ) 