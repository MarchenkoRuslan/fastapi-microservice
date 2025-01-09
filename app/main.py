from app.api.v1.api import api_router
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")
