from sqlalchemy.orm import Session
from app.services.client import ClientService

def test_get_by_binance_id(db: Session):
    client_service = ClientService(db)
    result = client_service.get_by_binance_id("test_id")
    assert result is None

def test_create_client(db: Session):
    client_service = ClientService(db)
    client = client_service.create(binance_user_id="test_id")
    assert client.binance_user_id == "test_id" 