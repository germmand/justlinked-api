from sqlalchemy import String, Column, Date, Integer, ForeignKey

from src.core.models import Base


class WorkExperience(Base):
    __tablename__ = 'work_experience'

    name = Column(String(100), nullable=False)
    description = Column(String(length=255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    applicant_id = Column(Integer, ForeignKey('applicants.id'))
