from flask import Blueprint, request, jsonify, current_app as app
from api.auth.models import User
import hashlib
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    new_user = request.get_json()
    user_exist = User.objects(email=new_user["email"])
    if user_exist:
        return jsonify(msg="User with email already registered", status=False), 400

    new_user["password"] = hashlib.sha256(
        new_user["password"].encode("utf-8")
    ).hexdigest()
    new_user = User(**new_user)
    new_user.save()
    return (
        jsonify(data=new_user.serialize(), msg="Registered successfully", status=True),
        201,
    )


@auth_bp.route("/login", methods=["POST"])
def login():
    payload = request.get_json()
    user = User.objects(email=payload.get("email")).first()
    if user:
        encrypted_pswd = hashlib.sha256(payload["password"].encode("utf-8")).hexdigest()
        if encrypted_pswd == user.password:
            access_token = create_access_token(identity=user.serialize())
            return jsonify(access_token=access_token, status=True), 200
    return jsonify(msg="Username or password is incorrect", status=False), 401
