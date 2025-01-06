import hashlib
import uuid
from datetime import datetime

from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = "clients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    binance_user_hash = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    orders = relationship("Order", back_populates="client")

    @staticmethod
    def generate_binance_hash(
        seller_name: str, seller_nickname: str, seller_mobile: str
    ) -> str:
        """Генерирует хеш на основе данных продавца из Binance."""
        combined = f"{seller_name}{seller_nickname}{seller_mobile}"
        return hashlib.md5(combined.encode()).hexdigest()
