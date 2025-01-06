import httpx
from typing import Optional, Dict, Any
from app.core.config import settings


class KYCProviderService:
    def __init__(self):
        self.api_key = settings.KYC_PROVIDER_API_KEY
        self.api_url = settings.KYC_PROVIDER_API_URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def create_verification_session(
        self,
        client_data: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Создает сессию верификации у KYC провайдера."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/verification/session",
                    json=client_data,
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error creating KYC session: {e}")
            return None

    async def check_verification_status(
        self,
        session_id: str
    ) -> Optional[Dict[str, Any]]:
        """Проверяет статус верификации."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.api_url}/verification/status/{session_id}",
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error checking verification status: {e}")
            return None 