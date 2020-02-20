from graphene_sqlalchemy import SQLAlchemyConnectionField

from .types import TechSkillType

all_tech_skills = SQLAlchemyConnectionField(TechSkillType)
