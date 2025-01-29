from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.client import Client
from app.services.client import ClientService


async def test_get_by_binance_id(db: Session):
    unique_id = str(uuid4())
    # Создаем клиента с уникальным binance_id
    client = Client(id=uuid4(), binance_id=f"test_binance_id_{unique_id}")
    db.add(client)
    db.commit()

    client_service = ClientService(db)
    result = client_service.get_by_binance_id(f"test_binance_id_{unique_id}")
    assert result.binance_id == f"test_binance_id_{unique_id}"


async def test_create_client(db: Session):
    unique_id = str(uuid4())
    client_service = ClientService(db)
    client = client_service.create(binance_id=f"test_binance_id_{unique_id}")
    assert client.binance_id == f"test_binance_id_{unique_id}"
