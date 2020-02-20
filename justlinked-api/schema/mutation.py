from sqlite3 import DatabaseError

import graphene
from database.models import (
    ApplicantModel
)
from schema.types import (
    ApplicantType
)


class ApplicantInput(graphene.InputObjectType):
    fullname = graphene.String(required=True)
    age = graphene.Int(required=True)
    address = graphene.String(required=True)
    country_of_residence = graphene.String(required=True)
    nacionality = graphene.String(required=True)
    email = graphene.String(required=True)
    salary_expectancy = graphene.Float(required=True)


class CreateApplicant(graphene.Mutation):
    class Arguments:
        applicant_data = ApplicantInput(required=True)

    ok = graphene.Boolean()
    applicant = graphene.Field(lambda: ApplicantType)

    def mutate(root, info, applicant_data=None):
        applicant = ApplicantModel(**applicant_data)
        try:
            applicant.save()
        except DatabaseError as e:
            applicant.__rollback()
            return CreateApplicant(applicant=None, ok=False, errors=str(e))
        return CreateApplicant(applicant=applicant, ok=True)


class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()
