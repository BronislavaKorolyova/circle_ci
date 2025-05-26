from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)

def test_submit_and_get_moods():
    # Submit a mood
    response = client.post("/submit", data={"mood": "happy", "note": "Great day"})
    assert response.status_code == 200
    assert response.json() == {"success": True}

    # Check mood log
    response = client.get("/moods")
    assert response.status_code == 200
    data = response.json()
    assert "entries" in data
    assert len(data["entries"]) > 0
    assert data["entries"][-1]["mood"] == "happy"

