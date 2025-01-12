# Standard library imports
from unittest.mock import AsyncMock, patch

# Third-party imports
import pytest

# Local imports
from app.services.binance import BinanceService


@pytest.mark.asyncio
async def test_get_user_order_detail_success():
    # Подготавливаем тестовые данные
    mock_response = {
        "orderNumber": "123456789",
        "status": "COMPLETED",
        "amount": 100.0,
        "fiat": "USD",
        "crypto": "BTC",
        "createTime": 1645084800000,
        "updateTime": 1645084800000,
    }

    # Создаем мок для ответа
    mock_response_obj = AsyncMock()
    mock_response_obj.status_code = 200
    mock_response_obj.json.return_value = mock_response

    # Используем обычный with вместо async with
    with patch(
        "app.services.binance.BinanceService.get_user_order_detail",
        return_value=mock_response,
    ) as mock_get:
        service = BinanceService()
        result = await service.get_user_order_detail("123456789")

        assert result == mock_response
        mock_get.assert_called_once_with("123456789")


@pytest.mark.asyncio
async def test_get_user_order_detail_not_found():
    # Используем обычный with вместо async with
    with patch(
        "app.services.binance.BinanceService.get_user_order_detail",
        side_effect=Exception("Order not found"),
    ) as mock_get:
        service = BinanceService()
        with pytest.raises(Exception, match="Order not found"):
            await service.get_user_order_detail("non_existent")

        mock_get.assert_called_once_with("non_existent")
