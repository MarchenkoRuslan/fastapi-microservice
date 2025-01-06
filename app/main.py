from app.api.v1.router import api_router
from fastapi import FastAPI

app = FastAPI(
    title="KYC Service API",
    description="API сервис для верификации клиентов и обработки заказов",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

app.include_router(api_router)
