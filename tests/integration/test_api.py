from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ping_integration():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json()["message"] == "pong"

def test_hello_integration():
    response = client.get("/hello")
    assert response.status_code == 200
    assert "Hello, world!" in response.json()["message"]
    assert "port" in response.json()["message"]

def test_add_integration():
    response = client.get("/add?a=10&b=15")
    assert response.status_code == 200
    assert response.json()["result"] == 25

def test_status_integration():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
