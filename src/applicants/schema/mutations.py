import graphene
from graphql import GraphQLError
from sqlalchemy.exc import DatabaseError

from src.core.config import db_session
from src.applicants.models import ApplicantModel, GeneralKnowledge, WorkExperience
from src.applicants.schema.types import ApplicantType
from src.tech_skills.models import ApplicantTechSkills


class GeneralKnowledgeInput(graphene.InputObjectType):
    description = graphene.String(required=True)


class WorkExperienceInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=True)
    start_date = graphene.Date(required=True)
    end_date = graphene.Date(required=True)


class ApplicantTechSkillInput(graphene.InputObjectType):
    skill_id = graphene.Int(required=True)
    experience_years = graphene.Int(required=True)


class ApplicantInput(graphene.InputObjectType):
    fullname = graphene.String(required=True)
    age = graphene.Int(required=True)
    address = graphene.String(required=True)
    country_of_residence = graphene.String(required=True)
    nacionality = graphene.String(required=True)
    email = graphene.String(required=True)
    salary_expectancy = graphene.Float(required=True)
    general_knowledge = graphene.List(GeneralKnowledgeInput, required=True)
    work_experience = graphene.List(WorkExperienceInput, required=True)
    tech_skills = graphene.List(ApplicantTechSkillInput, required=True)


class CreateApplicant(graphene.Mutation):
    class Arguments:
        applicant_data = ApplicantInput(required=True)

    ok = graphene.Boolean()
    applicant = graphene.Field(lambda: ApplicantType)

    def mutate(root, info, applicant_data=None):
        general_knowledge = applicant_data.pop('general_knowledge')
        work_experience = applicant_data.pop('work_experience')
        tech_skills = applicant_data.pop('tech_skills')

        applicant = ApplicantModel(**applicant_data)

        for k in general_knowledge:
            applicant.general_knowledge.append(GeneralKnowledge(**k))
        for we in work_experience:
            applicant.work_experience.append(WorkExperience(**we))

        try:
            applicant.save()
            [k.save() for k in applicant.general_knowledge]
            [we.save() for we in applicant.work_experience]
            [
                ApplicantTechSkills(**{'applicant_id': applicant.id, 'techskill_id': tk.skill_id,
                                       'experience_years': tk.experience_years}).save()
                for tk in tech_skills
            ]
            db_session.flush()
        except DatabaseError as e:
            raise GraphQLError(message=e)
        return CreateApplicant(applicant=applicant, ok=True)
