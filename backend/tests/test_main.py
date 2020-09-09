from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {
        "client_id": "test_id",
        "client_secret": "test_secret",
        "user_agent": "test_user_agent"
    }
