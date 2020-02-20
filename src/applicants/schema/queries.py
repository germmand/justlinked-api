# Set up the query type and compose them in root query type
from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.applicants.schema.types import ApplicantType

all_applicants = SQLAlchemyConnectionField(ApplicantType)
