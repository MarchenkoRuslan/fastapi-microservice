from uuid import uuid4

from app.models.client import Client
from app.models.profile import Profile
from app.models.verification import Verification
from sqlalchemy.orm import Session


def test_client_creation(db):
    # Создаем клиента
    client = Client(binance_id="test123")
    db.add(client)
    db.commit()

    # Проверяем, что клиент создан
    assert client.id is not None
    assert client.binance_id == "test123"
    assert len(client.profiles) == 0  # profiles вместо profile


def test_profile_creation(db):
    # Создаем клиента и профиль
    client = Client(binance_id="test123")
    db.add(client)
    db.commit()

    profile = Profile(name="Test User", client_id=client.id)
    db.add(profile)
    db.commit()

    # Проверяем связи
    assert profile.client_id == client.id
    assert len(client.profiles) == 1
    assert client.profiles[0].name == "Test User"


def test_verification_status_flow(db: Session):
    client = Client(id=uuid4(), binance_id=f"test_binance_id_{uuid4()}")
    db.add(client)

    verification = Verification(id=uuid4(), client_id=client.id, status="pending")
    db.add(verification)
    db.commit()

    assert verification.status == "pending"
    assert verification.client == client
