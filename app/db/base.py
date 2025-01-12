import os

from app.db.base_class import Base
from app.models.client import Client
from app.models.order import Order
from app.models.profile import Profile
from app.models.survey import Survey
from app.models.survey_response import SurveyResponse
from app.models.verification import Verification
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

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
