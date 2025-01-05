from fastapi import APIRouter
from app.api.v1.endpoints import webhooks, public, private

api_router = APIRouter()

api_router.include_router(
    public.router,
    prefix="/public",
    tags=["public"]
)

api_router.include_router(
    private.router,
    prefix="/private",
    tags=["private"]
) 