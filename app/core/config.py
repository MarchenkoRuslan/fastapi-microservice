from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # PostgreSQL
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = "kyc_service"
    
    # Binance
    BINANCE_API_KEY: str
    BINANCE_API_SECRET: str
    
    # KYC Provider
    KYC_PROVIDER_API_KEY: Optional[str] = None
    KYC_PROVIDER_API_URL: Optional[str] = None
    
    # Security
    JWT_SECRET_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings() 