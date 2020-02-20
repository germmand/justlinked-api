from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from src.core.models import Base

ApplicantTechSkills = Table('applicants_tech_skills', Base.metadata,
                            Column('applicant_id', Integer, ForeignKey('applicants.id')),
                            Column('techskill_id', Integer, ForeignKey('techskills.id')),
                            Column('experience_years', Integer))


class ApplicantModel(Base):
    __tablename__ = 'applicants'

    fullname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    country_of_residence = Column(String)
    email = Column(String, unique=True, nullable=False)
    nacionality = Column(String, nullable=False)
    modality_id = Column(Integer, ForeignKey('modality.id'))
    salary_expectancy = Column(Float, nullable=False)
    general_knowledge = relationship("GeneralKnowledge")
    work_experience = relationship("WorkExperience")
    tech_skills = relationship('TechSkillModel', secondary=ApplicantTechSkills)
