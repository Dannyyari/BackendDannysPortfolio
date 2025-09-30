import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_contact_api(client):
    response = client.post("/api/contact", json={
        "name": "John Doe",
        "email": "john.doe@gmail.com",
        "subject": "Testing subject",
        "message": "Hello, this is a test message."
    })

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "success"
    assert "message" in json_data

def clearNameWhenRecived(text):
    if text is None or text.isEmpty:
        return "empty message"
    return text

def clearEmailWhenRecived(text):
    if text is None or text.isEmpty:
        return "empty message"
    return text

def clearSubjectWhenRecived(text):
    if text is None or text.isEmpty:
        return "empty message"
    return text

def clearMessageWhenRecived(text):
    if text is None or text.isEmpty:
        return "empty message"
    return text