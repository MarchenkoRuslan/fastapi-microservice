from uuid import UUID

from . import BaseSchema


class SurveyResponse(BaseSchema):
    id: UUID
    title: str
    is_active: bool = True
