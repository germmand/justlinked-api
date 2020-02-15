from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from schema import schema
import database.models

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))
