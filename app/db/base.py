from sqlalchemy import create_engine
from app.core.config import settings


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_SERVER}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL) 