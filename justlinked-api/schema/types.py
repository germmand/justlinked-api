import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from database.models import ApplicantModel, TechSkillModel

class ApplicantType(SQLAlchemyObjectType):
    class Meta:
        model = ApplicantModel
        interfaces = (graphene.relay.Node,)

class TechSkillType(SQLAlchemyObjectType):
    class Meta:
        model = TechSkillModel
        interfaces = (graphene.relay.Node, )
