from uuid import uuid4

from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Client(Base):
    id = Column(UUID, primary_key=True, default=uuid4)
    binance_id = Column(String, unique=True, index=True)
    profiles = relationship("Profile", back_populates="client")
    orders = relationship("Order", back_populates="client")
    survey_responses = relationship("SurveyResponse", back_populates="client")
    verifications = relationship("Verification", back_populates="client")
