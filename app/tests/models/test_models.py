from datetime import date
from app.models.client import Client
from app.models.profile import Profile
from app.models.verification import Verification, VerificationStatus


def test_client_creation(db):
    client = Client(binance_user_id="test123", email="test@example.com")
    db.add(client)
    db.commit()

    assert client.id is not None
    assert client.created_at is not None
    assert client.updated_at is not None


def test_profile_creation(db):
    client = Client(binance_user_id="test123")
    db.add(client)
    db.commit()

    profile = Profile(
        client_id=client.id,
        first_name="John",
        last_name="Doe",
        birth_date=date(1990, 1, 1),
        country="US",
    )
    db.add(profile)
    db.commit()

    assert profile.id is not None
    assert profile.client_id == client.id


def test_verification_status_flow(db):
    client = Client(binance_user_id="test123")
    db.add(client)
    db.commit()

    verification = Verification(
        client_id=client.id,
        provider_session_id="session123",
        status=VerificationStatus.PENDING,
    )
    db.add(verification)
    db.commit()

    assert verification.status == VerificationStatus.PENDING

    verification.status = VerificationStatus.COMPLETED
    db.commit()

    updated_verification = db.query(Verification).first()
    assert updated_verification.status == VerificationStatus.COMPLETED
