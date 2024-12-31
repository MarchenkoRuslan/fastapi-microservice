from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from uuid import UUID
from datetime import datetime

class SurveyQuestionResponse(BaseModel):
    question_id: str
    answer: Any

class SurveySubmission(BaseModel):
    client_id: UUID
    survey_id: UUID
    responses: List[SurveyQuestionResponse]

class SurveyResult(BaseModel):
    score: int
    passed: bool
    details: Optional[Dict[str, Any]] = None

class SurveyData(BaseModel):
    id: UUID
    title: str
    content: Dict[str, Any]
    active: bool = True
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 