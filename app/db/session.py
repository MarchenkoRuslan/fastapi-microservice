import os
from typing import AsyncGenerator

from app.db.base import async_session_maker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
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


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
