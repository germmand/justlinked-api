import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from database.models import ApplicantModel, TechSkillModel, ModalityModel, PositionModel, GeneralKnowledge


class ApplicantType(SQLAlchemyObjectType):
    class Meta:
        model = ApplicantModel
        interfaces = (graphene.relay.Node,)

    general_knowledge = graphene.List(lambda: GeneralKnowledgeType)

    def resolve_general_knowledge(self, info):
        query = GeneralKnowledgeType.get_query(info)

        return query.all()


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


class GeneralKnowledgeType(SQLAlchemyObjectType):
    class Meta:
        model = GeneralKnowledge
        interfaces = (graphene.relay.Node,)
