from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

from database.session import db_session


class BaseModel():
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def save(self):
        db_session.add(self)
        db_session.commit()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


Base = declarative_base(cls=BaseModel)
Base.query = db_session.query_property()


class ModalityModel(Base):
    __tablename__ = 'modality'
    name = Column(String)
    applicants = relationship("ApplicantModel", backref="modality")
    positions = relationship("PositionModel", backref="modality")


ApplicantTechSkills = Table('applicants_tech_skills', Base.metadata,
                            Column('applicant_id', Integer, ForeignKey('applicants.id')),
                            Column('techskill_id', Integer, ForeignKey('techskills.id')),
                            Column('experience_years', Integer))

PositionTechSkills = Table('position_tech_skills', Base.metadata,
                           Column('position_id', Integer, ForeignKey('positions.id')),
                           Column('techskill_id', Integer, ForeignKey('techskills.id')))


class ApplicantModel(Base):
    __tablename__ = 'applicants'

    fullname = Column(String)
    age = Column(Integer)
    address = Column(String)
    country_of_residence = Column(String)
    nacionality = Column(String)
    modality_id = Column(Integer, ForeignKey('modality.id'))


class PositionModel(Base):
    __tablename__ = 'positions'

    name = Column(String)
    required_experience_years = Column(Integer)
    needs_travel = Column(Boolean)
    needs_relocation = Column(Boolean)
    modality_id = Column(Integer, ForeignKey('modality.id'))


class TechSkillModel(Base):
    __tablename__ = 'techskills'

    name = Column(String)
    applicants = relationship("ApplicantModel",
                              secondary=ApplicantTechSkills,
                              backref="techskills")
    positions = relationship("PositionModel",
                             secondary=PositionTechSkills,
                             backref="techskills")
