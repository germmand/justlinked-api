import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.positions.models import ModalityModel, PositionModel


class ModalityType(SQLAlchemyObjectType):
    class Meta:
        model = ModalityModel
        interfaces = (graphene.relay.Node,)


class PositionType(SQLAlchemyObjectType):
    class Meta:
        model = PositionModel
        interfaces = (graphene.relay.Node,)
