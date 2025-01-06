from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderCheckRequest(BaseModel):
    order_number: str = Field(
        ...,
        description="Номер ордера Binance P2P",
        min_length=5,
        max_length=50
    )

    class Config:
        json_schema_extra = {
            "example": {
                "order_number": "123456789"
            }
        }


class OrderCheckResponse(BaseModel):
    status: str = Field(..., description="Статус запроса (success/error)")
    data: Optional[Dict[str, Any]] = Field(None, description="Данные ордера")
    error: Optional[str] = Field(None, description="Сообщение об ошибке")

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "data": {
                    "orderNumber": "123456789",
                    "sellerName": "John Doe",
                    "sellerNickname": "johndoe",
                    "sellerMobilePhone": "+1234567890",
                    "status": "COMPLETED"
                }
            }
        } 