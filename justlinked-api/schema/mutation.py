from sqlite3 import DatabaseError

import graphene

from database.models import (
    ApplicantModel,
    GeneralKnowledge, WorkExperience)
from schema.types import (
    ApplicantType
)


class GeneralKnowledgeInput(graphene.InputObjectType):
    description = graphene.String(required=True)


class WorkExperienceInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=True)
    start_date = graphene.Date(required=True)
    end_date = graphene.Date(required=True)


class ApplicantInput(graphene.InputObjectType):
    fullname = graphene.String(required=True)
    age = graphene.Int(required=True)
    address = graphene.String(required=True)
    country_of_residence = graphene.String(required=True)
    nacionality = graphene.String(required=True)
    email = graphene.String(required=True)
    salary_expectancy = graphene.Float(required=True)
    general_knowledge = graphene.List(GeneralKnowledgeInput)
    work_experience = graphene.List(WorkExperienceInput)


class CreateApplicant(graphene.Mutation):
    class Arguments:
        applicant_data = ApplicantInput(required=True)

    ok = graphene.Boolean()
    applicant = graphene.Field(lambda: ApplicantType)

    def mutate(root, info, applicant_data=None):
        general_knowledge = applicant_data.pop('general_knowledge')
        work_experience = applicant_data.pop('work_experience')

        applicant = ApplicantModel(**applicant_data)

        for k in general_knowledge:
            applicant.general_knowledge.append(GeneralKnowledge(**k))
        for we in work_experience:
            applicant.work_experience.append(WorkExperience(**we))
        try:
            applicant.save()
            [k.save() for k in applicant.general_knowledge]
            [we.save() for we in applicant.work_experience]
        except DatabaseError as e:
            applicant.__rollback()
            return CreateApplicant(applicant=None, ok=False, errors=str(e))
        return CreateApplicant(applicant=applicant, ok=True)


class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()
