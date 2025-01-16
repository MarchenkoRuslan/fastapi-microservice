from app.db.session import get_session
from app.schemas.binance import OrderCheckRequest, OrderCheckResponse
from app.services.binance_service import BinanceService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/checkOrder", response_model=OrderCheckResponse)
async def check_order(
    request: OrderCheckRequest, session: AsyncSession = Depends(get_session)
) -> OrderCheckResponse:
    try:
        binance_service = BinanceService()
        order_details = await binance_service.get_user_order_detail(request.orderNumber)

        if not order_details:
            raise HTTPException(status_code=404, detail="Order not found")

        return OrderCheckResponse(status="success", data=order_details)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch order details: {str(e)}"
        )
