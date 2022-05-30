from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from config import config

jwt = JWTManager()
db = MongoEngine()
bcrypt = Bcrypt()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    with app.app_context():
        extensions(app)
        routes(app)

    return app


def extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)


def routes(app):
    from api.auth.views import auth_bp
    from api.template.views import template_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(template_bp)
