import pytest
from api.auth.models import User
from main import create_app
from mongoengine import connect
from mongoengine.connection import _get_db

connect("test", alias="test")


@pytest.fixture()
def app():
    app = create_app("testing")
    with app.app_context():
        yield app


@pytest.fixture()
def client(app):
    client = app.test_client()
    with app.app_context():
        yield client
        # drop collection after running client
        # this fixture should run per function and drop any record before the next function
        db = _get_db()
        db.drop_collection("user")
        db.drop_collection("template")


@pytest.fixture()
def create_user(client):
    return client.post(
        "/register",
        json={
            "first_name": "Dan",
            "last_name": "Taylor",
            "email": "dantaylor@sloovi.group",
            "password": "dantay100",
        },
    )

@pytest.fixture()
def token(create_user, client):
    resp = client.post('/login',
                       json={"email": "dantaylor@sloovi.group", "password": "dantay100"})
    token = resp.json['access_token']
    return token

@pytest.fixture()
def create_template(client, token):
    resp = client.post('/template', 
                       json={"template_name": "Test", "subject": "test subject", "body": "test_body"}, headers={'Authorization': f'Bearer {token}'})
    return resp.json
