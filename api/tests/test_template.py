invalid_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1NDUwMzk3NSwianRpIjoiMGE1OWEzZDUtY2U0Ny00NTM1LThiZWQtYTdhMzU5MDg1NjljIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJfaWQiOiI2Mjk3YTcxYjcxZGMxMGNlMDJiZjVmYjUiLCJmaXJzdF9uYW1lIjoiQXlvIiwibGFzdF9uYW1lIjoiT2xheWl3b2xhIiwiZW1haWwiOiJheW9vbGF5aXdvbGFAZ21haWwuY29tIn0sIm5iZiI6MTY1NDUwMzk3NSwiZXhwIjoxNjU0NTA0ODc1fQ.JxWeKXAL7zodCsXxSB0TwfjW_e2mB9Qa4nHfKF1_V2Y"


def test_create_template(client, token):
    resp = client.post(
        "/template",
        json={
            "template_name": "Template",
            "subject": "Evolution",
            "body": "Some template evolution here haha",
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert resp.status_code == 201
    assert "data" in resp.json


def test_create_template_invalid_payload(client, token):
    resp = client.post(
        "/template",
        json={
            "tempate_name": "Template",
            "subject": "Evolution",
            "b0dy": "Some template evolution here haha",
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert resp.status_code == 400
    assert "errors" in resp.json


def test_create_template_invalid_authorization(client):
    resp = client.post(
        "/template",
        json={
            "template_name": "Template",
            "subject": "Evolution",
            "body": "Some template evolution here haha",
        },
        headers={"Authorization": f"Bearer {invalid_token}"},
    )

    assert resp.status_code == 401
    assert "msg" in resp.json


def test_get_all_template(client, token):
    resp = client.get("/template", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    assert "results" in resp.json


def test_get_all_template_invalid_authorization(client):
    resp = client.get("/template", headers={"Authorization": f"Bearer {invalid_token}"})
    assert resp.status_code == 401
    assert "msg" in resp.json


# def test_get_all_template_forbidden_authorization(client):
#     resp = client.get("/template", headers={"Authorization": "Bearer "})
#     assert resp.status_code == 403
#     assert resp.json["msg"] == "Forbidden access to resource"


def test_get_single_template(client, token, create_template):
    temp = create_template["data"]
    resp = client.get(
        f"/template/{temp['_id']}", headers={"Authorization": f"Bearer {token}"}
    )
    assert resp.status_code == 200
    assert len(resp.json) == 2  # resp contains data and status
    assert isinstance(resp.json["data"], dict)


def test_get_single_template_invalid_id(client, token):
    resp = client.get(
        "/template/62978a4d5e41441d2cdcbf38",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 404
    assert resp.json["msg"] == "Template does not exist"


def test_update_template(client, token, create_template):
    temp = create_template["data"]
    resp = client.put(
        f"/template/{temp['_id']}",
        json={
            "template_name": "New Test",
            "subject": "New test subject",
            "body": "Changed test body",
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert resp.status_code == 200
    assert resp.json["data"]["_id"] == temp["_id"]
    assert resp.json["data"]["template_name"] == "New Test"
    assert resp.json["data"]["subject"] == "New test subject"
    assert resp.json["data"]["body"] == "Changed test body"


def test_update_template_invalid_id(client, token):
    resp = client.put(
        "/template/62978a4d5e41441d2cdcbf38",
        json={
            "template_name": "New Test",
            "subject": "New test subject",
            "body": "Changed test body",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 404
    assert resp.json["msg"] == "Template does not exist"


def test_update_template_invalid_authorization(client, create_template):
    temp = create_template["data"]
    resp = client.put(
        f"/template/{temp['_id']}",
        json={
            "template_name": "New Test",
            "subject": "New test subject",
            "body": "Changed test body",
        },
        headers={"Authorization": f"Bearer {invalid_token}"},
    )

    assert resp.status_code == 401
    assert "msg" in resp.json


def test_delete_template(client, token, create_template):
    temp = create_template["data"]
    resp = client.delete(
        f"/template/{temp['_id']}", headers={"Authorization": f"Bearer {token}"}
    )

    assert resp.status_code == 200
    assert resp.json["msg"] == "Deleted template successfully"


def test_delete_template_invalid_id(client, token):
    resp = client.delete(
        "/template/62978a4d5e41441d2cdcbf38",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert resp.status_code == 404
    assert resp.json["msg"] == "Template does not exist"


def test_delete_template_invalid_authorization(client, create_template):
    temp = create_template["data"]
    resp = client.delete(
        f"/template/{temp['_id']}", headers={"Authorization": f"Bearer {invalid_token}"}
    )

    assert resp.status_code == 401
    assert "msg" in resp.json
