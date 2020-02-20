import graphene

from src.applicants import all_applicants
from src.positions.schema.queries import all_positions
from src.tech_skills.schema.queries import all_tech_skills


class Query(graphene.ObjectType):
    applicants = all_applicants
    tech_skills = all_tech_skills
    positions = all_positions
