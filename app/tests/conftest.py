import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Загружаем .env.test
load_dotenv(".env.test")

# Используем переменные окружения
DATABASE_URL = "postgresql://postgres:9379992@localhost:5432/test_db"

# Создаем движок с echo=True для отладки SQL
engine = create_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def db():
    from app.db.base import Base

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    # Удаляем таблицы в правильном порядке
    Base.metadata.drop_all(
        bind=engine,
        tables=[
            Base.metadata.tables["verifications"],
            Base.metadata.tables["survey_responses"],
            Base.metadata.tables["profiles"],
            Base.metadata.tables["orders"],
            Base.metadata.tables["surveys"],
            Base.metadata.tables["clients"],
        ],
    )
