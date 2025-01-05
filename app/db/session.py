from typing import Generator
from sqlalchemy.orm import sessionmaker
from app.db.base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 