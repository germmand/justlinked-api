from sqlalchemy import create_engine
from src.database.config import DATABASE_URI

engine = create_engine(DATABASE_URI)
