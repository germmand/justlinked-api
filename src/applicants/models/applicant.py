from sqlalchemy import String, Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.core.models import Base


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
