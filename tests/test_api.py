import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.config.database import Base
from app.db.session import get_db
from app.main import app

# Use environment variable for test database URL, fallback to in-memory SQLite
TEST_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")

if TEST_DATABASE_URL.startswith("postgresql://"):
    # PostgreSQL test configuration
    engine = create_engine(TEST_DATABASE_URL)
else:
    # SQLite test configuration
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create test database tables
Base.metadata.create_all(bind=engine)


# Override the get_db dependency for testing
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_signal():
    response = client.post(
        "/signals/",
        json={"id": 1, "name": "test_signal"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "test_signal"
    assert data["aspects"] == []


def test_get_signals():
    response = client.get("/signals/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_create_aspect():
    # Create a signal first
    client.post(
        "/signals/",
        json={"id": 2, "name": "test_signal_2"},
    )

    # Create an aspect for the signal
    response = client.post(
        "/signals/2/aspects/",
        json={"type": "PERMISSIVE"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["type"] == "PERMISSIVE"
    assert data["is_on"] is False
    assert data["signal_id"] == 2


def test_update_aspect():
    # Create signal and aspect
    client.post(
        "/signals/",
        json={"id": 3, "name": "signal_for_update"},
    )
    response = client.post(
        "/signals/3/aspects/",
        json={"type": "PERMISSIVE"},
    )
    aspect_id = response.json()["id"]

    # Update the aspect state
    response = client.patch(
        f"/aspects/{aspect_id}",
        json={"is_on": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["is_on"] is True


def test_get_signal_aspects():
    # Create signal with multiple aspects
    client.post(
        "/signals/",
        json={"id": 4, "name": "multi_aspect_signal"},
    )
    client.post(
        "/signals/4/aspects/",
        json={"type": "PERMISSIVE"},
    )
    client.post(
        "/signals/4/aspects/",
        json={"type": "OVERRIDE"},
    )

    # Get all aspects for the signal
    response = client.get("/signals/4/aspects")
    assert response.status_code == 200
    data = response.json()
    assert data["signal_id"] == 4
    assert data["signal_name"] == "multi_aspect_signal"
    assert len(data["aspects"]) == 2

    # Verify aspect types
    aspect_types = [aspect["type"] for aspect in data["aspects"]]
    assert "PERMISSIVE" in aspect_types
    assert "OVERRIDE" in aspect_types


def test_mutual_exclusivity():
    # Create signal
    client.post(
        "/signals/",
        json={"id": 5, "name": "exclusivity_test"},
    )

    # Create PERMISSIVE and RESTRICTIVE aspects
    perm_response = client.post(
        "/signals/5/aspects/",
        json={"type": "PERMISSIVE"},
    )
    rest_response = client.post(
        "/signals/5/aspects/",
        json={"type": "RESTRICTIVE"},
    )

    perm_id = perm_response.json()["id"]
    rest_id = rest_response.json()["id"]

    # Turn on PERMISSIVE
    response = client.patch(
        f"/aspects/{perm_id}",
        json={"is_on": True},
    )
    assert response.status_code == 200

    # Try to turn on RESTRICTIVE (should fail)
    response = client.patch(
        f"/aspects/{rest_id}",
        json={"is_on": True},
    )
    assert response.status_code == 400
    assert "Cannot turn ON" in response.json()["detail"]


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    expected_response = {
        "message": "Welcome to Signal Equipment API",
        "status": "running",
        "version": "1.0.0",
        "ci_cd": "enabled",
    }
    assert response.json() == expected_response


@pytest.fixture(autouse=True)
def cleanup_database():
    """Clean up database after each test"""
    yield
    # Clean up tables after each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
