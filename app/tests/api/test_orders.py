from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app


def test_check_order_success():
    mock_response = {
        "orderNumber": "123456789",
        "status": "COMPLETED",
        "amount": 100.0,
        "fiat": "USD",
        "crypto": "BTC",
        "createTime": 1645084800000,
        "updateTime": 1645084800000,
    }

    with patch(
        "app.services.binance_service.BinanceService.get_user_order_detail",
        new_callable=AsyncMock,
    ) as mock_get:
        mock_get.return_value = mock_response

        client = TestClient(app)
        response = client.post("/api/v1/checkOrder", json={"orderNumber": "123456789"})

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["data"] == mock_response


def test_check_order_not_found():
    with patch(
        "app.services.binance_service.BinanceService.get_user_order_detail",
        new_callable=AsyncMock,
    ) as mock_get:
        mock_get.return_value = None

        client = TestClient(app)
        response = client.post(
            "/api/v1/checkOrder", json={"orderNumber": "non_existent"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "error"
        assert "not found" in data["error"].lower()
