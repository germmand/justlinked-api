import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from database.models import ApplicantModel, TechSkillModel, ModalityModel, PositionModel


class ApplicantType(SQLAlchemyObjectType):
    class Meta:
        model = ApplicantModel
        interfaces = (graphene.relay.Node,)


class TechSkillType(SQLAlchemyObjectType):
    class Meta:
        model = TechSkillModel
        interfaces = (graphene.relay.Node,)


class ModalityType(SQLAlchemyObjectType):
    class Meta:
        model = ModalityModel
        interfaces = (graphene.relay.Node,)


class PositionType(SQLAlchemyObjectType):
    class Meta:
        model = PositionModel
        interfaces = (graphene.relay.Node,)
