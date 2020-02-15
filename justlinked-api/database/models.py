from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from database.engine import engine
from database.session import db_session

class BaseModel():
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def save(self):
        db_session.add(self)
        db_session.commit()

Base = declarative_base(cls=BaseModel)
Base.query = db_session.query_property()

class ApplicantModel(Base):
    __tablename__ = 'applicants'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    age = Column(Integer)
    address = Column(String)
    country_of_residence = Column(String)
    nacionality = Column(String)

class TechSkillModel(Base):
    __tablename__ = 'techskills'

    id = Column(Integer, primary_key=True)
    name = Column(String)

ApplicantTechSkills = Table('applicants_tech_skills', Base.metadata,
    Column('applicant_id', Integer, ForeignKey('applicants.id')),
    Column('techskill_id', Integer, ForeignKey('techskills.id')))
