from fastapi.testclient import TestClient

from python.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {
        "client_id": "jonahjones094@gmail.com",
        "client_secret": "Dyerl236",
        "user_agent": "1234"
    }