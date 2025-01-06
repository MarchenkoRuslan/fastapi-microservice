from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any
from app.db.session import get_db


router = APIRouter()


@router.get("/profile")
async def get_profile(db: Session = Depends(get_db)) -> Any:
    """Получает профиль текущего пользователя."""
    # TODO: Implement profile retrieval
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/profile")
async def update_profile(db: Session = Depends(get_db)) -> Any:
    """Обновляет профиль пользователя."""
    # TODO: Implement profile update
    raise HTTPException(status_code=501, detail="Not implemented")
