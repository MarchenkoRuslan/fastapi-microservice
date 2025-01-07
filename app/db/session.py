import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Получаем DATABASE_URL из переменных окружения
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:9379992@localhost:5432/test_db"
)

# Создаем движок
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
