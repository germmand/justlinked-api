from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from src.schema import schema
from src.core.config.config import Config

from src.auth.google import router as google_router

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=schema))
@app.get("/")
async def redirect_root_to_graphql():
    url = Config.HOST + '/graphql'
    response = RedirectResponse(url=url)
    return response

app.include_router(google_router,
                   prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
def upgrade():
    from os import environ
    from scripts.alembic_helper import upgrade_latest
    if environ.get('GENERATE_DATA') and environ.get('MIGRATE'):
        upgrade_latest(True)
    elif environ.get('MIGRATE'):
        upgrade_latest(False)
