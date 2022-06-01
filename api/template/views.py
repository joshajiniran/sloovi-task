from api.template.models import Template
from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from mongoengine.errors import DoesNotExist, NotUniqueError, FieldDoesNotExist

template_bp = Blueprint("template", __name__)


@template_bp.route("/template", methods=["POST"])
@jwt_required()
def create_template():
    try:
        current_user = get_jwt_identity()
        payload = request.get_json()
        payload.update({"owner": current_user["_id"]})
        template = Template(**payload)
        template.save()
        return (
            jsonify(
                data=template.serialize(),
                status=True,
                msg="Created template successfully",
            ),
            201,
        )
    except NotUniqueError as e:
        return jsonify(msg="Template already exist", status=False), 400
    except FieldDoesNotExist as e:
        return jsonify(msg="Invalid payload", errors=str(e), status=False), 400


@template_bp.route("/template", methods=["GET"])
@jwt_required()
def get_all_templates():
    current_user = get_jwt_identity()

    templates = Template.objects(owner=current_user["_id"]).all()
    return (
        jsonify(results=[template.serialize() for template in templates], status=True),
        200,
    )


@template_bp.route("/template/<id>", methods=["GET"])
@jwt_required()
def get_template(id: int):
    try:
        current_user = get_jwt_identity()
        template = Template.objects.get(id=id, owner=current_user["_id"])
        return jsonify(data=template.serialize(), status=True), 200
    except DoesNotExist:
        return jsonify(msg="Template does not exist", status=False), 404


@template_bp.route("/template/<id>", methods=["PUT"])
@jwt_required()
def update_template(id: int):
    try:
        body = request.get_json()
        current_user = get_jwt_identity()
        template = Template.objects.get(id=id, owner=current_user["_id"])
        template.update(**body)
        template.reload()
        return (
            jsonify(
                data=template.serialize(),
                status=True,
                msg="Updated template successfully",
            ),
            200,
        )
    except NotUniqueError:
        return jsonify(msg="Template already exist", status=False), 400
    except DoesNotExist:
        return jsonify(msg="Template does not exist", status=False), 404
    except FieldDoesNotExist as e:
        return jsonify(msg="Invalid payload", errors=str(e), status=False), 400


@template_bp.route("/template/<id>", methods=["DELETE"])
@jwt_required()
def delete_template(id: int):
    try:
        current_user = get_jwt_identity()
        template = Template.objects.get(id=id, owner=current_user["_id"])
        template.delete()
        return jsonify(msg="Deleted template successfully", status=True), 200
    except DoesNotExist:
        return jsonify(msg="Template does not exist", status=False), 404
