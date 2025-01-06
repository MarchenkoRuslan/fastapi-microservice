from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ProfileBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None
    country: Optional[str] = None
    address: Optional[str] = None


class ProfileCreate(ProfileBase):
    client_id: UUID


class ProfileUpdate(ProfileBase):
    pass


class ProfileInDB(ProfileBase):
    id: UUID
    client_id: UUID

    class Config:
        from_attributes = True
