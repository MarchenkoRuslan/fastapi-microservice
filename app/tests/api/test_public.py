from unittest.mock import AsyncMock, patch

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_check_order_success():
    with patch(
        "app.services.binance_service.BinanceService.get_user_order_detail",
        new_callable=AsyncMock,
    ) as mock_get_order:
        mock_get_order.return_value = {"orderNumber": "123", "status": "COMPLETED"}
        response = client.get("/api/v1/public/check-order/123")
        assert response.status_code == 200
        assert response.json()["status"] == "COMPLETED"


def test_check_order_not_found():
    with patch(
        "app.services.binance_service.BinanceService.get_user_order_detail",
        new_callable=AsyncMock,
    ) as mock_get_order:
        mock_get_order.return_value = None
        response = client.get("/api/v1/public/check-order/123")
        assert response.status_code == 404


def test_check_order_with_id():
    with patch(
        "app.services.binance_service.BinanceService.get_user_order_detail",
        new_callable=AsyncMock,
    ) as mock_get_order:
        mock_get_order.return_value = {"orderNumber": "123", "status": "COMPLETED"}
        response = client.get("/api/v1/public/check-order/123?client_id=456")
        assert response.status_code == 200
        assert response.json()["status"] == "COMPLETED"
