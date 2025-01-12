from app.db.session import get_session
from app.schemas.binance import OrderCheckRequest, OrderCheckResponse
from app.services.binance_service import BinanceService
from fastapi import APIRouter, Depends
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
            return OrderCheckResponse(
                status="error",
                error="Order not found",
                message="The specified order was not found",
            )

        return OrderCheckResponse(status="success", data=order_details)

    except Exception as e:
        return OrderCheckResponse(
            status="error", error=str(e), message="Failed to fetch order details"
        )
