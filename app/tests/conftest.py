import pytest
from typing import AsyncGenerator, Generator
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from app.db.base import Base
from app.main import app


SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:9379992@localhost/kyc_service_test"
)


def create_test_database():
    temp_engine = create_engine(
        "postgresql://postgres:9379992@localhost/postgres"
    )
    with temp_engine.connect() as conn:
        conn.execute(text("COMMIT"))  # Закрыть текущую транзакцию
        conn.execute(text("DROP DATABASE IF EXISTS kyc_service_test"))
        conn.execute(text("CREATE DATABASE kyc_service_test"))


try:
    create_test_database()
except OperationalError:
    print("Warning: Could not create test database. It might already exist.")


engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture(scope="function")
async def db() -> AsyncGenerator[Session, None]:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c 