import uvicorn as asgi
from os import environ

from src import app
from .alembic_helper import upgrade_latest


def run_app(app, port=8000, host='0.0.0.0'):
    return asgi.run(app, port=port, host=host)


def run_production():
    if environ['GENERATE_DATA']:
        upgrade_latest(generate_data=True)
    else:
        upgrade_latest()
    return run_app(app)
