from sqlalchemy.orm import Session


class BinanceService:
    def __init__(self, db: Session = None):
        self.db = db

    @staticmethod
    async def get_user_order_detail(order_id: str):
        # Заглушка для тестов
        return {"orderNumber": order_id, "status": "COMPLETED"}
