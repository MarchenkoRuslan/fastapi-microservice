from uuid import UUID

from . import BaseSchema


class VerificationResponse(BaseSchema):
    id: UUID
    status: str
    client_id: UUID
