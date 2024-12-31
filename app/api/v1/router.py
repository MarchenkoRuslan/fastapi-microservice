from fastapi import APIRouter
from api.v1.endpoints import public, private

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