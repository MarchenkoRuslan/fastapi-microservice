from sqlalchemy.orm import Session
from app.services.survey import SurveyService
from app.models.survey import Survey
from uuid import uuid4

def test_get_active_survey(db: Session):
    survey_service = SurveyService(db)
    result = survey_service.get_active_survey()
    assert result is None

def test_calculate_score(db: Session):
    survey_service = SurveyService(db)
    responses = [{"question": "test", "answer": "test"}]
    survey = Survey(id=uuid4(), questions=[{"text": "test"}])
    score = survey_service.calculate_score(responses, survey)
    assert isinstance(score, int) 