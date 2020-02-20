from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from src.schema import schema

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))


@app.on_event('startup')
def upgrade():
    from os import environ
    from scripts.alembic_helper import upgrade_latest
    if environ.get('GENERATE_DATA') and environ.get('MIGRATE'):
        upgrade_latest(True)
    elif environ.get('MIGRATE'):
        upgrade_latest(False)
