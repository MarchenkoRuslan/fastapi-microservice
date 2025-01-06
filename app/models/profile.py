import uuid

from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"))

    # Поля от KYC провайдера
    phone = Column(String)
    country = Column(String)
    region = Column(String)
    city = Column(String)
    full_name = Column(String)

    # Поля от Binance
    binance_seller_name = Column(String)
    binance_seller_nickname = Column(String)
    binance_seller_mobile_phone = Column(String)

    client = relationship("Client", back_populates="profile")
