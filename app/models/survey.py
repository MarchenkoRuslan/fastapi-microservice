from uuid import uuid4

from sqlalchemy import UUID, Boolean, Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Survey(Base):
    id = Column(UUID, primary_key=True, default=uuid4)
    title = Column(String)
    is_active = Column(Boolean, default=True)

    responses = relationship("SurveyResponse", back_populates="survey")
