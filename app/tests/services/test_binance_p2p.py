from unittest.mock import AsyncMock, patch

import pytest
from app.services.binance_p2p import BinanceP2PService

pytestmark = pytest.mark.asyncio


async def test_get_p2p_order():
    with patch("aiohttp.ClientSession.get") as mock_get:
        # Создаем мок для ответа
        mock_response = AsyncMock()
        mock_response.raise_for_status = AsyncMock()
        mock_response.json.return_value = {"orderNumber": "123", "status": "COMPLETED"}

        # Настраиваем контекстный менеджер
        mock_get.return_value.__aenter__.return_value = mock_response

        service = BinanceP2PService()
        result = await service.get_p2p_order("123")

        assert result["orderNumber"] == "123"
        assert result["status"] == "COMPLETED"
