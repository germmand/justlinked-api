from sqlalchemy import Column, String, Integer, ForeignKey

from src.core.models import Base


class GeneralKnowledge(Base):
    __tablename__ = 'general_knowledge'

    description = Column(String(length=255), nullable=False)
    applicant_id = Column(Integer, ForeignKey('applicants.id'))
