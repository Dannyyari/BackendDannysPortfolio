from main import app

def clearNameWhenRecived(text):
    if not text:
        return "empty message"
    return text

def clearEmailWhenRecived(text):
    if not text:
        return "empty message"
    return text

def clearSubjectWhenRecived(text):
    if not text:
        return "empty message"
    return text

def clearMessageWhenRecived(text):
    if not text:
        return "empty message"
    return text


def test_clearNameWhenRecived():
    assert clearNameWhenRecived("John") == "John"
    assert clearNameWhenRecived("") == "empty message"

def test_clearEmailWhenRecived():
    assert clearEmailWhenRecived("john.doe@gmail.com") == "john.doe@gmail.com"
    assert clearEmailWhenRecived("") == "empty message"

def test_clearSubjectWhenRecived():
    assert clearSubjectWhenRecived("Testing subject") == "Testing subject"
    assert clearSubjectWhenRecived("") == "empty message"




#@pytest.fixture
#def client():
#    with app.test_client() as client:
#        yield client

#def test_contact_api(client):
#    response = client.post("/api/contact", json={
#        "name": "John Doe",
#        "email": "john.doe@gmail.com",
#        "subject": "Testing subject",
#        "message": "Hello, this is a test message."
#    })
#
#    assert response.status_code == 200
#    json_data = response.get_json()
#    assert json_data["status"] == "success"
#    assert "message" in json_data