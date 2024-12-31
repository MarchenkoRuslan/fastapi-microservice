import pytest
from unittest.mock import patch
from uuid import uuid4

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_check_order_not_found(client):
    response = client.get("/api/v1/public/check-order/nonexistent")
    assert response.status_code == 200
    assert response.json() == {
        "order_exists": False,
        "needs_verification": False,
        "client_id": None,
        "message": "Order not found",
        "details": None
    }

@patch('services.binance.BinanceService.get_order')
def test_check_order_new_client(mock_get_order, client, test_order):
    mock_get_order.return_value = test_order
    
    response = client.get(f"/api/v1/public/check-order/{test_order['orderId']}")
    assert response.status_code == 200
    data = response.json()
    
    assert data["order_exists"] is True
    assert data["needs_verification"] is True
    assert "client_id" in data
    assert data["message"] == "Verification required"
    assert "user_data" in data["details"]

@patch('services.binance.BinanceService.get_order')
def test_check_order_existing_client(mock_get_order, client, test_order):
    # Сначала создаем клиента
    mock_get_order.return_value = test_order
    first_response = client.get(f"/api/v1/public/check-order/{test_order['orderId']}")
    client_id = first_response.json()["client_id"]
    
    # Теперь проверяем повторный запрос
    response = client.get(f"/api/v1/public/check-order/{test_order['orderId']}")
    assert response.status_code == 200
    data = response.json()
    
    assert data["order_exists"] is True
    assert data["needs_verification"] is True
    assert data["client_id"] == client_id 