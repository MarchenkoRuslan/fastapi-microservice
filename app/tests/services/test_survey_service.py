from sqlalchemy.orm import Session
from app.services.survey import SurveyService
from app.models.survey import Survey
from uuid import uuid4


def test_get_active_survey(db: Session):
    # Создаем активный опрос
    survey = Survey(id=uuid4(), title="Test Survey", is_active=True)
    db.add(survey)
    db.commit()

    survey_service = SurveyService(db)
    result = survey_service.get_active_survey()
    assert result is not None
    assert result.is_active is True


def test_calculate_score(db: Session):
    survey_service = SurveyService(db)
    responses = [{"question": "test", "answer": "test"}]

    # Создаем опрос с вопросами через колонку JSON
    survey = Survey(id=uuid4(), title="Test Survey")
    survey.questions = [{"text": "test"}]  # Устанавливаем вопросы после создания

    score = survey_service.calculate_score(responses, survey)
    assert isinstance(score, int)
