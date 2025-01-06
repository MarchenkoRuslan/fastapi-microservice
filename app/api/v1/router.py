from fastapi import APIRouter

from app.api.v1.endpoints import private, public

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(public.router, prefix="/public", tags=["public"])

api_router.include_router(private.router, prefix="/private", tags=["private"])
