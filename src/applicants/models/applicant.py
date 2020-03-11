from sqlalchemy import String, Column, Integer, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

from src.core.models import Base


class ApplicantModel(Base):
    __tablename__ = 'applicants'

    photo = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    address = Column(String)
    country_of_residence = Column(String)
    email = Column(String, unique=True, nullable=False)
    nacionality = Column(String)
    modality_id = Column(Integer, ForeignKey('modality.id'))
    salary_expectancy = Column(Float)
    general_knowledge = relationship("GeneralKnowledge")
    work_experience = relationship("WorkExperience")
