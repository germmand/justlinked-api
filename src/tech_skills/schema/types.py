import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.tech_skills.models.tech_skills import TechSkillModel


class TechSkillType(SQLAlchemyObjectType):
    class Meta:
        model = TechSkillModel
        interfaces = (graphene.relay.Node,)
