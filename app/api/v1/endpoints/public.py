from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any
from app.db.session import get_db
from app.services.binance import BinanceService
from app.schemas.binance import OrderCheckRequest, OrderCheckResponse

router = APIRouter()


@router.post("/checkOrder", response_model=OrderCheckResponse)
async def check_order(
    request: OrderCheckRequest,
    db: Session = Depends(get_db)
) -> Any:
    """
    Проверяет существование ордера в Binance P2P.
    
    Args:
        request: OrderCheckRequest с номером ордера
    
    Returns:
        OrderCheckResponse с информацией об ордере и продавце
        
    Raises:
        HTTPException: если ордер не найден или произошла ошибка
    """
    try:
        binance_service = BinanceService()
        order_data = await binance_service.get_user_order_detail(request.order_number)
        
        return OrderCheckResponse(
            status="success",
            data=order_data
        )
    except Exception as e:
        return OrderCheckResponse(
            status="error",
            error=str(e)
        ) 