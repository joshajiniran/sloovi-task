import os
from ensurepip import version

from dotenv import load_dotenv
from flask.cli import FlaskGroup

from main import create_app

load_dotenv()

env = os.getenv("FLASK_ENV")

app = create_app(env)


@app.route("/", methods=["GET"])
def health():
    return {
        "api": "Sloovi API",
        "version": "0.1.0",
        "status": True,
        "msg": "Server is active",
        "status_code": 200,
    }


cli = FlaskGroup(app)

# any cli command

if __name__ == "__main__":
    cli()
