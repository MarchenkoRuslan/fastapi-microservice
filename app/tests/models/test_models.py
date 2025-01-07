from uuid import uuid4

from app.models.client import Client
from app.models.profile import Profile
from app.models.verification import Verification
from sqlalchemy.orm import Session


def test_client_creation(db: Session):
    client = Client(id=uuid4(), binance_id=f"test_binance_id_{uuid4()}")
    db.add(client)
    db.commit()
    db.refresh(client)

    assert client.binance_id.startswith("test_binance_id_")
    assert client.orders == []
    assert client.survey_responses == []
    assert client.verifications == []
    assert client.profile is None


def test_profile_creation(db: Session):
    client = Client(id=uuid4(), binance_id=f"test_binance_id_{uuid4()}")
    db.add(client)

    profile = Profile(id=uuid4(), client_id=client.id)
    db.add(profile)
    db.commit()

    assert profile.client_id == client.id
    assert profile.client == client


def test_verification_status_flow(db: Session):
    client = Client(id=uuid4(), binance_id=f"test_binance_id_{uuid4()}")
    db.add(client)

    verification = Verification(id=uuid4(), client_id=client.id, status="pending")
    db.add(verification)
    db.commit()

    assert verification.status == "pending"
    assert verification.client == client
