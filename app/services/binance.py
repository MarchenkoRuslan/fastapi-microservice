import hashlib
import hmac
import time
from typing import Any, Dict

import httpx

from app.core.config import settings
from app.core.logger import logger


class BinanceService:
    def __init__(self):
        self.api_key = settings.BINANCE_API_KEY
        self.api_secret = settings.BINANCE_SECRET_KEY
        self.base_url = settings.BINANCE_API_HOST

    def _generate_signature(self, params: Dict[str, Any]) -> str:
        """Генерирует подпись для запроса к Binance API."""
        query_string = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

    async def get_user_order_detail(self, order_number: str) -> Dict[str, Any]:
        """
        Получает детальную информацию об ордере.

        Args:
            order_number: Номер ордера для проверки

        Returns:
            Dict с информацией об ордере

        Raises:
            Exception: если ордер не найден или произошла ошибка
        """
        try:
            timestamp = int(time.time() * 1000)
            params = {"orderNumber": order_number, "timestamp": timestamp}

            signature = self._generate_signature(params)
            params["signature"] = signature

            headers = {"X-MBX-APIKEY": self.api_key, "Content-Type": "application/json"}

            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/sapi/v1/c2c/orderMatch/getUserOrderDetail",
                    params=params,
                    headers=headers,
                )

                if response.status_code == 404:
                    raise Exception("Order not found")

                response.raise_for_status()
                return response.json()

        except Exception as e:
            logger.error(f"Error getting order details: {e}")
            raise
