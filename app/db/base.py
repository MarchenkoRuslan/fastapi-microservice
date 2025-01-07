from app.db.base_class import Base
from app.models.client import Client
from app.models.order import Order
from app.models.profile import Profile
from app.models.survey import Survey
from app.models.survey_response import SurveyResponse
from app.models.verification import Verification

# Определяем порядок создания таблиц
__all__ = [
    "Base",
    "Client",
    "Profile",
    "Survey",
    "Order",
    "Verification",
    "SurveyResponse",
]
