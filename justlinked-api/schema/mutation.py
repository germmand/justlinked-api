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

class CreateApplicant(graphene.Mutation):
    class Arguments:
        applicant_data = ApplicantInput(required=True)

    ok = graphene.Boolean()
    applicant = graphene.Field(lambda: ApplicantType)

    def mutate(root, info, applicant_data=None):
        applicant = ApplicantModel(
            fullname=applicant_data.fullname,
            age=applicant_data.age,
            address=applicant_data.address,
            country_of_residence=applicant_data.country_of_residence,
            nacionality=applicant_data.nacionality
        )
        # TODO: Validar que se agregó correctamente.
        applicant.save()
        ok = True
        return CreateApplicant(applicant=applicant, ok=ok)

class Mutation(graphene.ObjectType):
    create_applicant = CreateApplicant.Field()
