import os

from dotenv import load_dotenv
from flask.cli import FlaskGroup

from main import create_app

load_dotenv()

env = os.getenv("FLASK_ENV")

app = create_app(env)

cli = FlaskGroup(app)

# any cli command

if __name__ == "__main__":
    cli()
