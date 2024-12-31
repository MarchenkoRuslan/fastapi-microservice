from binance.spot import Spot
from core.config import settings
from typing import Optional, Dict, Any

class BinanceService:
    def __init__(self):
        self.client = Spot(
            api_key=settings.BINANCE_API_KEY,
            api_secret=settings.BINANCE_API_SECRET
        )
    
    async def get_order(self, order_id: str) -> Optional[Dict[str, Any]]:
        """
        Получает информацию о заказе из Binance
        """
        try:
            # Здесь нужно реализовать правильный вызов API Binance
            # Это пример, который нужно адаптировать под реальное API
            order = self.client.get_order(orderId=order_id)
            return order
        except Exception as e:
            # Логирование ошибки
            print(f"Error getting order from Binance: {e}")
            return None 