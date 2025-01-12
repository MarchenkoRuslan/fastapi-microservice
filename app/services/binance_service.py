import hashlib
import hmac
import os
import time
from typing import Dict, Optional

import httpx


class BinanceService:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")
        self.base_url = os.getenv("BINANCE_API_HOST")

    def _generate_signature(self, params: Dict) -> str:
        """Генерирует подпись для запроса к Binance API"""
        query_string = "&".join(
            [f"{key}={params[key]}" for key in sorted(params.keys())]
        )
        signature = hmac.new(
            self.secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return signature

    async def get_user_order_detail(self, order_number: str) -> Optional[Dict]:
        """Получает детали ордера из Binance API"""
        timestamp = int(time.time() * 1000)
        params = {"timestamp": timestamp, "orderNumber": order_number}

        signature = self._generate_signature(params)
        params["signature"] = signature

        headers = {"X-MBX-APIKEY": self.api_key}

        url = f"{self.base_url}/sapi/v1/c2c/orderMatch/getUserOrderDetail"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers)

            if response.status_code == 404:
                return None

            response.raise_for_status()
            return response.json()
