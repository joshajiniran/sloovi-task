import hashlib

from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from mongoengine.errors import ValidationError

from api.auth.models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        new_user = request.get_json()
        user_exist = User.objects(email=new_user["email"])
        if user_exist:
            return jsonify(msg="User with email already registered", status=False), 400

        new_user["password"] = User.make_password(new_user["password"])
        new_user = User(**new_user)
        new_user.save()
        return (
            jsonify(
                data=new_user.serialize(), msg="Registered successfully", status=True
            ),
            201,
        )
    except ValidationError:
        return jsonify(msg="Validation error: invalid payload", status=False), 422


@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        payload = request.get_json()
        user = User.objects(email=payload.get("email")).first()
        if user:
            if user.check_password(payload.get("password")):
                access_token = create_access_token(identity=user.serialize())
                return jsonify(access_token=access_token, status=True), 200
        return jsonify(msg="Username or password is incorrect", status=False), 401
    except ValidationError:
        return jsonify(msg="Validation error: invalid payload", status=False), 422
