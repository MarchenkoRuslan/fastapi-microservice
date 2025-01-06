from app.services.binance import BinanceService
import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
async def test_get_user_order_detail():
    mock_response = {
        "data": {
            "orderNumber": "123456",
            "sellerName": "TestSeller",
            "sellerNickname": "test_nick",
            "sellerMobilePhone": "+1234567890",
        }
    }

    with patch(
        "app.services.binance.BinanceService.get_user_order_detail",
        return_value=mock_response,
    ) as mock:
        result = await mock("123456")
        assert result == mock_response


@pytest.mark.asyncio
async def test_get_user_order_detail_not_found():
    service = BinanceService()

    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value.status_code = 404

        with pytest.raises(Exception) as exc_info:
            await service.get_user_order_detail("invalid")

        assert "Order not found" in str(exc_info.value)
