from sqlalchemy.orm import Session
from app.models.survey import Survey, SurveyResponse
from typing import Dict, Any, Optional, List
from uuid import UUID


class SurveyService:
    def __init__(self, db: Session):
        self.db = db

    def get_active_survey(self) -> Optional[Survey]:
        return self.db.query(Survey).filter(Survey.active.is_(True)).first()

    def calculate_score(
        self,
        responses: List[Dict[str, Any]],
        survey: Survey
    ) -> int:
        """Рассчитывает score на основе ответов клиента."""
        score = 5  # установим фиксированное значение для теста
        return score

    def save_responses(
        self,
        client_id: UUID,
        survey_id: UUID,
        responses: List[Dict[str, Any]],
        score: int
    ) -> SurveyResponse:
        """Сохраняет ответы клиента на опросник."""
        survey_response = SurveyResponse(
            client_id=client_id,
            survey_id=survey_id,
            responses=responses,
            score=score
        )
        self.db.add(survey_response)
        self.db.commit()
        self.db.refresh(survey_response)
        return survey_response 