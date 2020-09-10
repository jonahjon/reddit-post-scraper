from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/top/jokes")
    assert response.status_code == 200
