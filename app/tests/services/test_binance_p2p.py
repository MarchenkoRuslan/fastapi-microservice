import pytest
from unittest.mock import patch, AsyncMock
from app.services.binance_p2p import BinanceP2PClient

@pytest.mark.asyncio
@patch('httpx.AsyncClient')
async def test_get_p2p_order(mock_async_client):
    # Создаем экземпляр клиента
    client = BinanceP2PClient()
    
    # Создаем мок для ответа
    mock_response = AsyncMock()
    mock_response.json = lambda: {"data": {"orderStatus": "pending"}}
    mock_response.raise_for_status = AsyncMock()
    
    # Создаем мок для клиента
    mock_client = AsyncMock()
    mock_client.post.return_value = mock_response
    
    # Настраиваем контекстный менеджер
    mock_async_client.return_value.__aenter__.return_value = mock_client
    mock_async_client.return_value.__aexit__.return_value = None
    
    # Вызываем метод и ждем результат
    result = await client.get_p2p_order("test_order_number")
    
    # Проверяем результат
    assert result == {"data": {"orderStatus": "pending"}}
    
    # Проверяем, что был сделан правильный запрос
    assert mock_client.post.called
    call_args = mock_client.post.call_args
    
    # Проверяем URL
    assert call_args[0][0] == "https://p2p.binance.com/bapi/c2c/v1/private/get-order"
    
    # Проверяем заголовки
    assert "X-MBX-APIKEY" in call_args[1]["headers"]
    assert call_args[1]["headers"]["Content-Type"] == "application/json"
    
    # Проверяем параметры
    assert "orderNumber" in call_args[1]["json"]
    assert "timestamp" in call_args[1]["json"] 