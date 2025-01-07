import pytest
from app.models.survey import Survey
from app.services.survey import SurveyService

pytestmark = pytest.mark.asyncio


async def test_get_active_survey(db):
    # Создаем тестовый опрос
    survey = Survey(title="Test Survey", is_active=True)
    db.add(survey)
    db.commit()

    service = SurveyService(db)
    active_survey = await service.get_active_survey()

    assert active_survey is not None
    assert active_survey.title == "Test Survey"


async def test_calculate_score():
    service = SurveyService()
    answers = {"q1": "yes", "q2": "no"}
    score = await service.calculate_score(answers)
    assert isinstance(score, int)
