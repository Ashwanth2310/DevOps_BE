from fastapi.testclient import TestClient
from main import app, PORT

def test_ping():
    client = TestClient(app)
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_hello():
    client = TestClient(app)
    response = client.get("/hello")
    assert response.status_code == 200
    expected = {"message": f"Hello, world! Running on port {PORT}"}
    assert response.json() == expected

def test_add():
    client = TestClient(app)
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_status():
    client = TestClient(app)
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
