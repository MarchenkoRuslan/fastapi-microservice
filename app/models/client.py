from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
import uuid

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
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