import pytest
from unittest.mock import patch, AsyncMock
from app.services.binance_p2p import BinanceP2PClient

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_get_p2p_order():
    # Создаем экземпляр клиента
    client = BinanceP2PClient()
    
    # Создаем мок для httpx.AsyncClient
    mock_response = AsyncMock()
    mock_response.json.return_value = {"data": {"orderStatus": "pending"}}
    mock_response.raise_for_status = AsyncMock()
    
    mock_client = AsyncMock()
    mock_client.post = AsyncMock(return_value=mock_response)
    
    mock_async_client = AsyncMock()
    mock_async_client.__aenter__.return_value = mock_client
    mock_async_client.__aexit__.return_value = None
    
    # Устанавливаем мок
    with patch('httpx.AsyncClient', return_value=mock_async_client):
        # Вызываем метод
        result = await client.get_p2p_order("test_order_number")
        
        # Проверяем результат
        assert result == {"data": {"orderStatus": "pending"}}
        
        # Проверяем, что был сделан правильный запрос
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        
        # Проверяем URL
        assert call_args[0][0] == "https://p2p.binance.com/bapi/c2c/v1/private/get-order"
        
        # Проверяем заголовки
        assert "X-MBX-APIKEY" in call_args[1]["headers"]
        assert call_args[1]["headers"]["Content-Type"] == "application/json"
        
        # Проверяем параметры
        assert "orderNumber" in call_args[1]["json"]
        assert "timestamp" in call_args[1]["json"] 