from unittest.mock import patch
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


@patch('app.services.binance.BinanceService.get_order')
def test_check_order_success(mock_get_order, client, db):
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
        status="pending"
    )
    db.add(test_order)
    db.commit()

    # Настраиваем мок
    mock_get_order.return_value = {"status": "pending"}

    # Проверяем ордер через API
    response = client.get(f"/api/v1/public/orders/check/{order_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "pending"
    assert data["data"] is not None
    assert "client_id" in data["data"]


def test_check_order_with_id(client, db):
    order_id = str(uuid4())
    response = client.get(f"/api/v1/public/orders/check/{order_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "pending"
    assert "client_id" in data 