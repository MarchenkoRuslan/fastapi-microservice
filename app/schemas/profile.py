from uuid import UUID

from . import BaseSchema


class ProfileBase(BaseSchema):
    name: str | None = None


class ProfileCreate(ProfileBase):
    client_id: UUID


class ProfileUpdate(ProfileBase):
    pass


class ProfileInDB(ProfileBase):
    id: UUID
    client_id: UUID

    class Config:
        from_attributes = True
