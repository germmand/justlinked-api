from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.ext.declarative import declarative_base

from src.core.config.session import db_session as session


@as_declarative()
class BaseModel(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def save(self):
        session.add(self)
        self._flush()
        session.commit()
        return self

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def delete(self):
        session.delete(self)
        self._flush()
        session.commit()

    def _flush(self):
        try:
            session.flush()
        except DatabaseError:
            session.rollback()
            raise


Base = declarative_base(cls=BaseModel)
Base.query = session.query_property()
