from sqlalchemy.orm import Session
from app.models.client import Client
from app.models.profile import Profile
from typing import Optional, Dict, Any
from uuid import UUID

class ClientService:
    def __init__(self, db: Session):
        self.db = db
    
    async def get_by_binance_id(self, binance_id: str) -> Optional[Client]:
        return self.db.query(Client).filter(
            Client.binance_user_id == binance_id
        ).first()
    
    async def create_from_binance(self, binance_data: Dict[str, Any]) -> Client:
        """
        Создает нового клиента на основе данных из Binance
        """
        client = Client(
            binance_user_id=binance_data.get("userId"),
            # Другие поля, которые мы можем получить из Binance
        )
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client
    
    @property
    def is_verified(self) -> bool:
        """
        Проверяет, верифицирован ли клиент
        """
        # Здесь нужно реализовать логику проверки верификации
        return False 