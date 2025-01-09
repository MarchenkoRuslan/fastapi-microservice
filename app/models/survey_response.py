from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import JSON, UUID, Column, ForeignKey
from sqlalchemy.orm import relationship


class SurveyResponse(Base):
    id = Column(UUID, primary_key=True, default=uuid4)
    survey_id = Column(UUID, ForeignKey("survey.id"))
    client_id = Column(UUID, ForeignKey("client.id"))
    answers = Column(JSON)

    survey = relationship("Survey", back_populates="responses")
    client = relationship("Client", back_populates="survey_responses")
