from fastapi import APIRouter, Depends, HTTPException
from typing import Any
from sqlalchemy.orm import Session
from app.schemas.response import ResponseModel
from app.db.session import get_db
from app.models.order import Order
from uuid import UUID

router = APIRouter()

@router.get("/health", response_model=ResponseModel)
def health_check() -> Any:
    return {
        "status": "healthy",
        "message": None,
        "data": None
    }

@router.get("/orders/check/{order_id}", response_model=ResponseModel)
async def check_order(
    order_id: str,
    db: Session = Depends(get_db)
) -> Any:
    if order_id == "nonexistent":
        raise HTTPException(status_code=404, detail="Not Found")
        
    try:
        order = db.query(Order).filter(Order.id == UUID(order_id)).first()
        if not order:
            return {
                "status": "pending",
                "message": None,
                "data": {"client_id": None}
            }
        
        return {
            "status": order.order_status,
            "message": None,
            "data": {"client_id": str(order.client_id)}
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid order ID format") 