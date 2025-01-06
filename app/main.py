from fastapi import FastAPI
from app.api.v1.router import api_router


app = FastAPI(
    title="P2P Trading Service",
    description="Service for P2P trading operations with Binance integration",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(api_router) 