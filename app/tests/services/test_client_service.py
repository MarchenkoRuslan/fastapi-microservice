import pytest
from services.client import ClientService
from models.client import Client

def test_create_client(db):
    service = ClientService(db)
    binance_data = {
        "userId": "test123",
        "email": "test@example.com"
    }
    
    client = service.create_from_binance(binance_data)
    assert client.binance_user_id == "test123"
    
    # Проверяем, что клиент сохранен в БД
    db_client = service.get_by_binance_id("test123")
    assert db_client is not None
    assert db_client.id == client.id

def test_get_nonexistent_client(db):
    service = ClientService(db)
    client = service.get_by_binance_id("nonexistent")
    assert client is None 