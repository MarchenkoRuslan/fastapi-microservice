from fastapi import APIRouter, Depends, HTTPException
from typing import Any
from sqlalchemy.orm import Session
from app.schemas.response import ResponseModel
from app.db.session import get_db
from app.services.binance import BinanceService

router = APIRouter()


@router.post("/checkOrder", response_model=ResponseModel)
async def check_order(
    order_number: str,
    db: Session = Depends(get_db)
) -> Any:
    """
    Проверяет существование ордера в Binance P2P.
    
    Args:
        order_number: Номер ордера для проверки
    
    Returns:
        Информация об ордере и продавце
    """
    try:
        binance_service = BinanceService()
        order_data = await binance_service.get_user_order_detail(order_number)
        
        return {
            "status": "success",
            "message": None,
            "data": order_data
        }
    except Exception as e:
        raise HTTPException(
            status_code=404 if "Order not found" in str(e) else 500,
            detail=str(e)
        ) 