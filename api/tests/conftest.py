import pytest

from main import create_app


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


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
