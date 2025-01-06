import pytest
from unittest.mock import patch, AsyncMock


@pytest.mark.asyncio
async def test_check_order_success(client):
    mock_response = {
        "data": {
            "orderNumber": "123456",
            "sellerName": "TestSeller",
            "sellerNickname": "test_nick",
            "sellerMobilePhone": "+1234567890",
        }
    }

    with patch(
        "app.services.binance.BinanceService.get_user_order_detail",
        new_callable=AsyncMock,
    ) as mock_get_order:
        mock_get_order.return_value = mock_response

        response = await client.post(
            "/api/v1/checkOrder", json={"order_number": "123456"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["data"] == mock_response


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
