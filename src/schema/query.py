import graphene

from src.applicants import all_applicants
from src.positions.schema.queries import all_positions
from src.tech_skills.schema.queries import all_tech_skills

from src.auth.decorators import jwt_required

class Query(graphene.ObjectType):
    applicants = all_applicants
    tech_skills = all_tech_skills
    positions = all_positions

    # This is placed here just for testing :) 
    me_email = graphene.String()

    @jwt_required
    def resolve_me_email(self, info):
        user = info.context["user"]
        return user.email