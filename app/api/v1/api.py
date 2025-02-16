from fastapi import APIRouter

from app.api.v1.endpoints import binance, orders, public

api_router = APIRouter()

api_router.include_router(binance.router, prefix="/binance", tags=["binance"])
api_router.include_router(public.router, prefix="/public", tags=["public"])
api_router.include_router(orders.router, tags=["orders"])
