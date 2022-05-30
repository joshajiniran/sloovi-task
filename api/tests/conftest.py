import pytest

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
def runner(app):
    return app.test_cli_runner()
