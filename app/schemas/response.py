from . import BaseSchema


class ResponseBase(BaseSchema):
    status: str


class OrderCheckResponse(BaseSchema):
    order_exists: bool
    needs_verification: bool
    client_id: str | None = None
    message: str
    details: dict | None = None


class VerificationResponse(BaseSchema):
    status: str
    message: str
    session_url: str | None = None
