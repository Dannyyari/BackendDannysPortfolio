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
