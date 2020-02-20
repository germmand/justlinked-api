from sqlalchemy.orm import (
    sessionmaker,
    scoped_session
)
from src.database.engine import engine

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
