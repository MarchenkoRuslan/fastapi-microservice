from typing import Any, Dict, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.survey import Survey
from app.models.survey_response import SurveyResponse


class SurveyService:
    def __init__(self, db: Session = None):
        self.db = db

    async def get_active_survey(self) -> Survey:
        return self.db.query(Survey).filter(Survey.is_active == True).first()

    async def calculate_score(self, answers: dict) -> int:
        # Простая реализация подсчета очков
        return len(answers)

    def save_responses(
        self,
        client_id: UUID,
        survey_id: UUID,
        responses: List[Dict[str, Any]],
        score: int,
    ) -> SurveyResponse:
        """Сохраняет ответы клиента на опросник."""
        survey_response = SurveyResponse(
            client_id=client_id, survey_id=survey_id, responses=responses, score=score
        )
        self.db.add(survey_response)
        self.db.commit()
        self.db.refresh(survey_response)
        return survey_response
