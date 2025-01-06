from unittest.mock import patch
from uuid import uuid4


def test_health_check(client):
    response = client.get("/api/v1/public/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_check_order_not_found(client):
    response = client.get("/api/v1/public/orders/check/nonexistent")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


@patch('services.binance.BinanceService.get_order')
def test_check_order_success(mock_get_order, client, test_order):
    mock_get_order.return_value = test_order

    response = client.get(
        f"/api/v1/public/check-order/{test_order['orderId']}"
    )
    assert response.status_code == 200
    data = response.json()

    assert data["order_exists"] is True
    assert data["needs_verification"] is True
    assert "client_id" in data
    assert data["message"] == "Verification required"
    assert "user_data" in data["details"]


def test_check_order_with_id(client, db):
    order_id = str(uuid4())
    response = client.get(f"/api/v1/public/orders/check/{order_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "pending"
    assert "client_id" in data 