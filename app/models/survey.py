from sqlalchemy import Column, String, JSON, Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import uuid
from datetime import datetime


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String, nullable=True)
    questions = Column(JSON, default=list)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SurveyResponse(Base):
    __tablename__ = "survey_responses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"), nullable=False)
    survey_id = Column(UUID(as_uuid=True), ForeignKey("surveys.id"), nullable=False)

    responses = Column(JSONB, nullable=False)
    score = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

    client = relationship("Client", back_populates="survey_responses")
    survey = relationship("Survey")
