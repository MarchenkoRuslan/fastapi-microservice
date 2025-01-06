from pydantic import BaseModel
from typing import Optional, Dict, Any


class OrderCheckRequest(BaseModel):
    order_number: str


class OrderCheckResponse(BaseModel):
    status: str
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None 