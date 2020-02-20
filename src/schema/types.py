import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.database.models import (
    ApplicantModel, TechSkillModel,
    ModalityModel, PositionModel,
    GeneralKnowledge, WorkExperience
)


class ApplicantType(SQLAlchemyObjectType):
    class Meta:
        model = ApplicantModel
        interfaces = (graphene.relay.Node,)

    general_knowledge = graphene.List(lambda: GeneralKnowledgeType)
    work_experience = graphene.List(lambda: WorkExperienceType)

    def resolve_general_knowledge(self, info):
        query = GeneralKnowledgeType.get_query(info)

        return query.all()

    def resolve_work_experience(self, info):
        query = WorkExperienceType.get_query(info)

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


class WorkExperienceType(SQLAlchemyObjectType):
    class Meta:
        model = WorkExperience
        interfaces = (graphene.relay.Node,)
