def test_new_user_registration(client):
    resp = client.post(
        "/register",
        json={
            "first_name": "Mike",
            "last_name": "Tyson",
            "email": "miketee@sloovi.group",
            "password": "knockout100",
        },
    )
    assert resp.status_code == 201
    assert "data" in resp.json
    assert "password" not in resp.json["data"]


def test_duplicate_user_registration(client, create_user):
    resp = client.post(
        "/register",
        json={
            "first_name": "Dan",
            "last_name": "Taylor",
            "email": "dantaylor@sloovi.group",
            "password": "knockout100",
        },
    )
    assert resp.status_code == 400
    assert resp.json["msg"] == "User with email already registered"


def test_register_new_user_invalid_data(client):
    resp = client.post(
        "/register",
        json={
            "first_tname": "Dan",
            "last_name": "Someone",
            "emal": "danincorrectpswd.com",
            "password": "testpswd",
        },
    )
    assert resp.status_code == 400
    assert resp.json["msg"] == "Invalid payload"
    assert "errors" in resp.json


def test_register_new_user_wrong_payload(client):
    resp = client.post(
        "/register",
        json={
            "first_name": "Dan",
            "last_name": 12,
            "email": "danincorrectswd.com",
            "password": "testpswd",
        },
    )
    assert resp.status_code == 400
    assert resp.json["msg"] == "Validation error: invalid payload"
    assert "errors" in resp.json


def test_login_user_successful(client, create_user):
    resp = client.post(
        "/login",
        json={
            "email": "dantaylor@sloovi.group",
            "password": "dantay100",
        },
    )
    assert resp.status_code == 200
    assert "access_token" in resp.json
    assert len(resp.json["access_token"].split(".")) == 3


def test_login_user_fail(client):
    resp = client.post(
        "/login",
        json={
            "email": "miketee@sloovi.group",
            "password": "knockout100",
        },
    )
    assert resp.status_code == 401
    assert resp.json["msg"] == "Username or password is incorrect"


def test_login_user_invalid_payload(client):
    resp = client.post(
        "/login",
        json={
            "ema": "miketee@sloovi.group",
            "passw)rd": "knockout100",
        },
    )
    assert resp.status_code == 400
    assert resp.json["msg"] == "Invalid payload"
    assert "errors" in resp.json
