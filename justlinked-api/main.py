import uvicorn
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from schema import schema

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
