from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "KYC Service"
    
    POSTGRES_SERVER: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "app")
    
    BINANCE_API_KEY: str = os.getenv("BINANCE_API_KEY", "test_key")
    BINANCE_API_SECRET: str = os.getenv("BINANCE_API_SECRET", "test_secret")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "test_jwt_secret")
    KYC_PROVIDER_API_KEY: str = os.getenv("KYC_PROVIDER_API_KEY", "test_kyc_key")
    KYC_PROVIDER_API_URL: str = os.getenv("KYC_PROVIDER_API_URL", "http://test.com")

    class Config:
        case_sensitive = True


settings = Settings() 