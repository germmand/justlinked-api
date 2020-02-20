from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey, Boolean, Float
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

from database.session import db_session as session


class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def save(self):
        session.add(self)
        self._flush()
        return self

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def delete(self):
        session.delete(self)
        self._flush()

    def _flush(self):
        try:
            session.flush()
        except DatabaseError:
            session.rollback()
            raise


Base = declarative_base(cls=BaseModel)
Base.query = session.query_property()


class ModalityModel(Base):
    __tablename__ = 'modality'
    name = Column(String, nullable=False, unique=True)
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

    fullname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    country_of_residence = Column(String)
    email = Column(String, unique=True, nullable=False)
    nacionality = Column(String, nullable=False)
    modality_id = Column(Integer, ForeignKey('modality.id'))
    salary_expectancy = Column(Float, nullable=False)


class PositionModel(Base):
    __tablename__ = 'positions'

    name = Column(String)
    required_experience_years = Column(Integer)
    needs_travel = Column(Boolean)
    needs_relocation = Column(Boolean)
    modality_id = Column(Integer, ForeignKey('modality.id'))


class TechSkillModel(Base):
    __tablename__ = 'techskills'

    name = Column(String, unique=False, nullable=False)
    applicants = relationship("ApplicantModel",
                              secondary=ApplicantTechSkills,
                              backref="techskills")
    positions = relationship("PositionModel",
                             secondary=PositionTechSkills,
                             backref="techskills")
