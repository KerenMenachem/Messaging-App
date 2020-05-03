import pytest , requests


@pytest.fixture()
def session():
    with requests.Session() as s:
        yield s


def test_GetMessage_ByAppId(session):
    resp = session.get('http://localhost:5000/GetMessage?application_id=9')
    data = resp.json()
    flag=0
    for d in data:
        if d['user_id']!=9:
            flag=1
    assert flag!=1

def test_GetMessage_ByMessageId(session):
    resp = session.get('http://localhost:5000/GetMessage?message_id=1')
    data = resp.json()
    flag=0
    for d in data:
        if d['message_id']!=1:
            flag=1
    assert flag!=1

def test_GetMessage__BySessionId(session):
    resp = session.get('http://localhost:5000/GetMessage?session_id=2')
    data = resp.json()
    flag = 0
    for d in data:
        if d['session_id']!=2:
            flag=1
    assert flag!=1



def test_DeleteMessage_BySessionId(session):
    delete = session.get('http://localhost:5000/DeleteMessage?session_id=1')
    resp = session.get('http://localhost:5000/GetMessage?session_id=1')
    All = len(resp.json())
    assert All==0

def test_DeleteMessage_ByMessageId(session):
    delete = session.get('http://localhost:5000/DeleteMessage?message_id=3')
    resp = session.get('http://localhost:5000/GetMessage?message_id=3')
    All = len(resp.json())
    assert All==0

def test_DeleteMessage_ByAppId(session):
    delete = session.get('http://localhost:5000/DeleteMessage?application_id=6')
    resp = session.get('http://localhost:5000/GetMessage?application_id=6')
    All = len(resp.json())
    assert All==0