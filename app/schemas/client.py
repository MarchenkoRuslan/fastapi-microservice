from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional


class ClientBase(BaseModel):
    email: Optional[EmailStr] = None
    binance_user_id: Optional[str] = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass


class ClientInDB(ClientBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
