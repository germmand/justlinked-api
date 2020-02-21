import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.applicants.models import ApplicantModel, WorkExperience, GeneralKnowledge


class ApplicantType(SQLAlchemyObjectType):
    class Meta:
        model = ApplicantModel
        interfaces = (graphene.relay.Node,)

    general_knowledge = graphene.List(lambda: GeneralKnowledgeType)
    work_experience = graphene.List(lambda: WorkExperienceType)
    tech_skills = graphene.List(lambda: ApplicantTechSkill)

    def resolve_general_knowledge(self, info):
        query = GeneralKnowledgeType.get_query(info)

        return query.all()

    def resolve_work_experience(self, info):
        query = WorkExperienceType.get_query(info)

        return query.all()

    def resolve_tech_skill(self, info):
        return ApplicantModel.query.filter_by(id=self.id).join('tech_skills').all()


class GeneralKnowledgeType(SQLAlchemyObjectType):
    class Meta:
        model = GeneralKnowledge
        interfaces = (graphene.relay.Node,)


class WorkExperienceType(SQLAlchemyObjectType):
    class Meta:
        model = WorkExperience
        interfaces = (graphene.relay.Node,)


class ApplicantTechSkill(graphene.ObjectType):
    name = graphene.String(required=True)
    experience_years = graphene.Int(required=True)
