from pydantic import BaseModel
from typing import Optional, Any, Dict
from uuid import UUID

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