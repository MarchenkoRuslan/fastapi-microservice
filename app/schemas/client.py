from datetime import datetime
from uuid import UUID

from . import BaseSchema


class ClientBase(BaseSchema):
    binance_id: str


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
