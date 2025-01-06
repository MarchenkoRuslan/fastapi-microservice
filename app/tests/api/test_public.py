from unittest.mock import patch, AsyncMock, MagicMock
from uuid import uuid4
from app.models.client import Client
from app.models.order import Order


def test_health_check(client):
    response = client.get("/api/v1/public/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": None, "data": None}


def test_check_order_not_found(client):
    response = client.get("/api/v1/public/orders/check/nonexistent")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


@patch('app.services.binance_p2p.BinanceP2PClient')
@patch('app.services.binance.BinanceService.get_order')
async def test_check_order_success(mock_get_order, mock_p2p_client, client, db):
    # Настраиваем мок для BinanceP2PClient
    mock_instance = MagicMock()
    mock_instance.get_p2p_order = AsyncMock(
        return_value={"data": {"orderStatus": "pending"}}
    )
    mock_p2p_client.return_value = mock_instance

    # Создаем тестового клиента
    test_client = Client(
        binance_user_id="test_user",
        email="test@example.com"
    )
    db.add(test_client)
    db.commit()

    # Создаем тестовый ордер
    order_id = str(uuid4())
    test_order = Order(
        id=order_id,
        client_id=test_client.id,
        order_status="pending"
    )
    db.add(test_order)
    db.commit()

    # Настраиваем мок для BinanceService
    mock_get_order.return_value = {"status": "pending"}

    # Проверяем ордер через API
    response = client.get(f"/api/v1/public/orders/check/{order_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "pending"
    assert data["data"] is not None
    assert "client_id" in data["data"]


def test_check_order_with_id(client):
    order_id = str(uuid4())
    response = client.get(f"/api/v1/public/orders/check/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "pending"
    assert "client_id" in data["data"] 