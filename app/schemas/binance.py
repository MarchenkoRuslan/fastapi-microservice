from typing import Dict, Optional

from pydantic import BaseModel, Field


class OrderCheckRequest(BaseModel):
    orderNumber: str = Field(
        ..., description="Номер ордера Binance P2P", min_length=5, max_length=50
    )

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "data": {
                    "orderNumber": "123456789",
                    "sellerName": "John Doe",
                    "sellerNickname": "johndoe",
                    "sellerMobilePhone": "+1234567890",
                    "status": "COMPLETED",
                },
            }
        }


class OrderCheckResponse(BaseModel):
    status: str
    data: Optional[Dict] = None
    error: Optional[str] = None
    message: Optional[str] = None


class BinanceOrderDetail(BaseModel):
    orderNumber: str
    status: str
    amount: float
    fiat: str
    crypto: str
    createTime: int
    updateTime: int
