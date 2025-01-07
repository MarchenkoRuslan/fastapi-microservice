from unittest.mock import patch

import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.mark.asyncio
async def test_check_order_success():
    with patch(
        "app.services.binance_service.BinanceService.get_user_order_detail"
    ) as mock_get_order:
        mock_get_order.return_value = {"orderNumber": "123", "status": "COMPLETED"}
        response = client.get("/api/v1/binance/check-order/123")
        assert response.status_code == 200
        assert response.json()["status"] == "COMPLETED"


@pytest.mark.asyncio
async def test_check_order_not_found():
    with patch(
        "app.services.binance_service.BinanceService.get_user_order_detail"
    ) as mock_get_order:
        mock_get_order.return_value = None
        response = client.get("/api/v1/binance/check-order/123")
        assert response.status_code == 404
