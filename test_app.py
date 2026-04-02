import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
        
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
    
def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_json() == {
        "version": "1.2.14",
        "nextUpdate": "June 17, 2026"
    }
    
def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.get_json() == {
    "status": "operational",
    "services": {
        "vercel":   "ok",
        "supabase": "ok",
        "twilio":   "ok"
    }
}