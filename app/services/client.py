from typing import Any, Dict
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.client import Client


class ClientService:
    def __init__(self, db: Session):
        self.db = db

    def get_by_binance_id(self, binance_id: str) -> Client:
        """Получает клиента по Binance ID."""
        return self.db.query(Client).filter(Client.binance_id == binance_id).first()

    def create(self, binance_id: str) -> Client:
        """Создает нового клиента."""
        client = Client(id=uuid4(), binance_id=binance_id)
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
