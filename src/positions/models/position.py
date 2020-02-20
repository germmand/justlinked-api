from sqlalchemy import String, Column, Integer, ForeignKey, Boolean

from src.core import Base


class PositionModel(Base):
    __tablename__ = 'positions'

    name = Column(String)
    required_experience_years = Column(Integer)
    needs_travel = Column(Boolean)
    needs_relocation = Column(Boolean)
    modality_id = Column(Integer, ForeignKey('modality.id'))
