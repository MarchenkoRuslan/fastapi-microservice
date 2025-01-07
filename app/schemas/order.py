from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    order_id: str
