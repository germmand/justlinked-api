import graphene
from src.schema.query import Query
from src.schema.mutation import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
