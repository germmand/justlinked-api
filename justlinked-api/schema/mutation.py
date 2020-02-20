from sqlite3 import DatabaseError

import graphene

from database.models import (
    ApplicantModel,
    GeneralKnowledge)
from schema.types import (
    ApplicantType
)


class GeneralKnowledgeInput(graphene.InputObjectType):
    description = graphene.String(required=True)


class ApplicantInput(graphene.InputObjectType):
    fullname = graphene.String(required=True)
    age = graphene.Int(required=True)
    address = graphene.String(required=True)
    country_of_residence = graphene.String(required=True)
    nacionality = graphene.String(required=True)
    email = graphene.String(required=True)
    salary_expectancy = graphene.Float(required=True)
    general_knowledge = graphene.List(GeneralKnowledgeInput)


class CreateApplicant(graphene.Mutation):
    class Arguments:
        applicant_data = ApplicantInput(required=True)

    ok = graphene.Boolean()
    applicant = graphene.Field(lambda: ApplicantType)

    def mutate(root, info, applicant_data=None):
        general_knowledge = applicant_data.pop('general_knowledge')

        applicant = ApplicantModel(**applicant_data)

        for k in general_knowledge:
            applicant.general_knowledge.append(GeneralKnowledge(**k))
        try:
            applicant.save()
            [k.save() for k in applicant.general_knowledge]
        except DatabaseError as e:
            applicant.__rollback()
            return CreateApplicant(applicant=None, ok=False, errors=str(e))
        return CreateApplicant(applicant=applicant, ok=True)


class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()
