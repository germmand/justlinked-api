from sqlalchemy import String, Column, Integer, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

from src.core import Base

PositionTechSkills = Table('position_tech_skills', Base.metadata,
                           Column('position_id', Integer, ForeignKey('positions.id')),
                           Column('techskill_id', Integer, ForeignKey('techskills.id')))


class PositionModel(Base):
    __tablename__ = 'positions'

    name = Column(String)
    required_experience_years = Column(Integer)
    needs_travel = Column(Boolean)
    needs_relocation = Column(Boolean)
    modality_id = Column(Integer, ForeignKey('modality.id'))
    required_tech_skills = relationship('TechSkillModel', secondary=PositionTechSkills)
