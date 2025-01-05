from sqlalchemy import create_engine
from app.core.config import settings
from app.db.base_class import Base

# Импорты моделей
from app.models.client import Client
from app.models.survey import Survey

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}/{settings.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL) 