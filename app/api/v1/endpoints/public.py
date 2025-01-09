from app.services.binance_service import BinanceService
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/check-order/{order_id}")
async def check_order(order_id: str, client_id: str = None):
    order = await BinanceService.get_user_order_detail(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
