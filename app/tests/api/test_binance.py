from unittest.mock import AsyncMock, patch

import pytest


def test_check_order_success(client):
    response = client.post(
        "/api/v1/public/checkOrder",
        json={"order_number": "123456"},
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_check_order_not_found(client):
    with patch(
        "app.services.binance.BinanceService.get_user_order_detail",
        new_callable=AsyncMock,
    ) as mock_get_order:
        mock_get_order.side_effect = Exception("Order not found")

        response = await client.post(
            "/api/v1/checkOrder", json={"order_number": "invalid"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "error"
        assert "Order not found" in data["error"]
