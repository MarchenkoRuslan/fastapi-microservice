from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.client import ClientService

router = APIRouter()


@router.post("/kyc-webhook")
async def kyc_webhook(request: Request, db: Session = Depends(get_db)) -> Any:
    """Обработчик вебхуков от KYC провайдера."""
    try:
        payload = await request.json()

        # Здесь нужно добавить проверку подписи вебхука

        session_id = payload.get("session_id")
        status = payload.get("status")
        client_id = payload.get("client_id")

        if not all([session_id, status, client_id]):
            raise HTTPException(status_code=400, detail="Missing required fields")

        client_service = ClientService(db)
        await client_service.update_verification_status(
            client_id=client_id, session_id=session_id, status=status, details=payload
        )

        return {"status": "success"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
