from sqlalchemy import create_engine
from database.config import DATABASE_URI

engine = create_engine(DATABASE_URI)
