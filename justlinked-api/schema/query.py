import graphene
from schema.types import (
    ApplicantType,
    TechSkillType,
    PositionType
)


class Query(graphene.ObjectType):
    applicants = graphene.List(ApplicantType)
    tech_skills = graphene.List(TechSkillType)
    positions = graphene.List(PositionType)

    def resolve_applicants(self, info):
        query = ApplicantType.get_query(info)
        return query.all()

    def resolve_tech_skills(self, info):
        query = TechSkillType.get_query(info)
        return query.all()

    def resolve_positions(self, info):
        query = PositionType.get_query(info)
        return query.all()
