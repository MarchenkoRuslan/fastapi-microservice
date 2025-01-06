from sqlalchemy.orm import Session
from app.models.client import Client
from typing import Optional, Dict, Any


class ClientService:
    def __init__(self, db: Session):
        self.db = db

    def get_by_binance_id(self, binance_id: str) -> Optional[Client]:
        """Получает клиента по Binance ID."""
        return (
            self.db.query(Client).filter(Client.binance_user_id == binance_id).first()
        )

    def create(self, binance_user_id: str) -> Client:
        """Создает нового клиента."""
        client = Client(binance_user_id=binance_user_id)
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def create_from_binance(self, binance_data: Dict[str, Any]) -> Client:
        """Создает клиента из данных Binance."""
        client = Client(
            binance_user_id=binance_data.get("userId"), email=binance_data.get("email")
        )
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client
