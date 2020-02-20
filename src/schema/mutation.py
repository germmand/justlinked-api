import graphene

from src.applicants import CreateApplicant


class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()
