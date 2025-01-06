from fastapi import FastAPI
from app.api.v1.router import api_router


app = FastAPI(
    title="KYC Service",
    description="Service for client verification and order processing",
    version="1.0.0"
)

app.include_router(api_router) 