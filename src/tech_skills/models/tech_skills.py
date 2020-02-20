from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.core.models import Base

ApplicantTechSkills = Table('applicants_tech_skills', Base.metadata,
                            Column('applicant_id', Integer, ForeignKey('applicants.id')),
                            Column('techskill_id', Integer, ForeignKey('techskills.id')),
                            Column('experience_years', Integer))

PositionTechSkills = Table('position_tech_skills', Base.metadata,
                           Column('position_id', Integer, ForeignKey('positions.id')),
                           Column('techskill_id', Integer, ForeignKey('techskills.id')))


class TechSkillModel(Base):
    __tablename__ = 'techskills'

    name = Column(String, unique=False, nullable=False)
    applicants = relationship("ApplicantModel",
                              secondary=ApplicantTechSkills,
                              backref="techskills")
    positions = relationship("PositionModel",
                             secondary=PositionTechSkills,
                             backref="techskills")
