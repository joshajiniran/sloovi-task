def test_register_new_user(client):
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
