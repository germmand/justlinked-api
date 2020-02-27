from sqlalchemy import Column, String

from src.core.models import Base


class TechSkillModel(Base):
    __tablename__ = 'techskills'

    name = Column(String, unique=False, nullable=False)
