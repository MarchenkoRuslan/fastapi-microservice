from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.base import Base
import uuid
from datetime import datetime

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Базовые поля для клиента
    email = Column(String, unique=True, index=True, nullable=True)
    binance_user_id = Column(String, unique=True, index=True, nullable=True) 
    
    # Relationships
    profile = relationship("Profile", back_populates="client", uselist=False)
    verifications = relationship("Verification", back_populates="client")
    orders = relationship("Order", back_populates="client")
    survey_responses = relationship("SurveyResponse", back_populates="client") 