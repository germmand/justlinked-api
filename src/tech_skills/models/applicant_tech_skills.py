from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.core.models import Base


class ApplicantTechSkills(Base):
    __tablename__ = 'applicants_tech_skills'

    id = None
    applicant_id = Column('applicant_id', Integer, ForeignKey('applicants.id'), primary_key=True)
    techskill_id = Column('techskill_id', Integer, ForeignKey('techskills.id'))
    applicants = relationship('ApplicantModel', backref='techskills')
    techskills = relationship('TechSkillModel')
    experience_years = Column('experience_years', Integer)
