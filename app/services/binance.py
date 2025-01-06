from typing import Optional, Dict, Any
from app.services.binance_p2p import BinanceP2PClient


class BinanceService:
    def __init__(self):
        self.p2p_client = BinanceP2PClient()

    async def get_order(self, order_id: str) -> Optional[Dict[str, Any]]:
        """Получает информацию об ордере из Binance P2P."""
        return await self.p2p_client.get_p2p_order(order_id)

    async def get_available_trades(
        self,
        fiat: str = "RUB",
        trade_type: str = "BUY",
        asset: str = "USDT"
    ) -> Optional[Dict[str, Any]]:
        """Получает список доступных P2P предложений."""
        return await self.p2p_client.get_p2p_trades(
            fiat=fiat,
            trade_type=trade_type,
            asset=asset
        ) 