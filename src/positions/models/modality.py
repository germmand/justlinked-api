from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.core import Base


class ModalityModel(Base):
    __tablename__ = 'modality'
    name = Column(String, nullable=False, unique=True)
    applicants = relationship("ApplicantModel", backref="modality")
    positions = relationship("PositionModel", backref="modality")
