import pytest
from services.survey import SurveyService
from models.survey import Survey
from uuid import uuid4

def test_get_active_survey(db):
    # Создаем тестовый опросник
    survey = Survey(
        id=uuid4(),
        title="Test Survey",
        content={
            "questions": [
                {
                    "id": "q1",
                    "text": "Test question",
                    "type": "choice",
                    "options": ["A", "B", "C"]
                }
            ],
            "minimum_score": 5
        },
        active=True
    )
    db.add(survey)
    db.commit()
    
    service = SurveyService(db)
    active_survey = service.get_active_survey()
    
    assert active_survey is not None
    assert active_survey.title == "Test Survey"
    assert active_survey.active is True

def test_calculate_score(db):
    survey = Survey(
        id=uuid4(),
        title="Test Survey",
        content={
            "questions": [
                {
                    "id": "q1",
                    "correct_answer": "A",
                    "score": 5
                }
            ],
            "minimum_score": 5
        },
        active=True
    )
    db.add(survey)
    db.commit()
    
    service = SurveyService(db)
    responses = [
        {"question_id": "q1", "answer": "A"}
    ]
    
    score = service.calculate_score(responses, survey)
    assert score == 5 