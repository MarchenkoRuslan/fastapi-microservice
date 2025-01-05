from pydantic import BaseModel
from typing import Optional, Any, Dict
from uuid import UUID
from app.db.session import get_db
from app.db.base import Base

class OrderCheckResponse(BaseModel):
    order_exists: bool
    needs_verification: bool
    client_id: Optional[UUID] = None
    message: str
    details: Optional[Dict[str, Any]] = None

class VerificationResponse(BaseModel):
    status: str
    session_url: Optional[str] = None
    message: str 