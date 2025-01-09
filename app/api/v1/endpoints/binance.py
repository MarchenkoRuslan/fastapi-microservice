from app.db.session import get_db
from app.services.binance_service import BinanceService
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/check-order/{order_id}")
async def check_order(order_id: str, db=Depends(get_db)):
    binance_service = BinanceService(db)
    order = await binance_service.get_user_order_detail(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
