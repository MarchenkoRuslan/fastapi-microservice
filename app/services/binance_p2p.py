import hmac
import hashlib
import time
from typing import Dict, Any, Optional
import httpx
from app.core.config import settings
from app.core.logger import logger


class BinanceP2PClient:
    def __init__(self):
        self.api_key = settings.BINANCE_API_KEY
        self.api_secret = settings.BINANCE_API_SECRET
        self.base_url = "https://api.binance.com"
        self.p2p_url = "https://p2p.binance.com/bapi/c2c"

    def _generate_signature(self, params: Dict[str, Any]) -> str:
        """Генерирует подпись для запроса."""
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

    async def get_p2p_order(self, order_number: str) -> Optional[Dict[str, Any]]:
        """Получает информацию о P2P ордере."""
        try:
            timestamp = int(time.time() * 1000)
            params = {"orderNumber": order_number, "timestamp": timestamp}

            headers = {"X-MBX-APIKEY": self.api_key, "Content-Type": "application/json"}

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.p2p_url}/v1/private/get-order", json=params, headers=headers
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Error getting P2P order: {e}")
            return None

    async def get_p2p_trades(
        self,
        fiat: str = "RUB",
        trade_type: str = "BUY",
        asset: str = "USDT",
        rows: int = 10,
    ) -> Optional[Dict[str, Any]]:
        """Получает список доступных P2P предложений."""
        try:
            params = {
                "fiat": fiat,
                "tradeType": trade_type,
                "asset": asset,
                "rows": rows,
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.p2p_url}/v1/public/ads", json=params
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Error getting P2P trades: {e}")
            return None
