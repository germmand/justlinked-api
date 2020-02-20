import graphene

from src.schema.mutation import Mutation
from src.schema.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
