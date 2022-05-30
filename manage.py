from flask.cli import FlaskGroup

from main import create_app

app = create_app()

cli = FlaskGroup(app)

# any cli command

if __name__ == "__main__":
    cli()
