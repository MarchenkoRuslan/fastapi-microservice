import logging
from typing import Any, Dict, Optional

import aiohttp
import httpx

logger = logging.getLogger(__name__)


class BinanceP2PService:
    def __init__(self):
        self.base_url = "https://api.binance.com/api/v1/p2p"

    async def get_p2p_order(self, order_number: str) -> dict:
        """
        Получение информации о P2P ордере
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/{order_number}") as response:
                    await response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            logger.error(f"Error getting P2P order: {e}")
            raise

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
