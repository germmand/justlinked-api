from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from src.schema import schema

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))
