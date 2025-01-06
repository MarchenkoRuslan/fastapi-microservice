from pydantic import BaseModel
from typing import Optional, Any, Dict

class ResponseModel(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[Dict[str, Any]] = None

class OrderCheckResponse(BaseModel):
    order_exists: bool
    needs_verification: bool
    client_id: Optional[str] = None
    message: str
    details: Optional[Dict[str, Any]] = None

class VerificationResponse(BaseModel):
    status: str
    message: str
    session_url: Optional[str] = None 