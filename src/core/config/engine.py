from sqlalchemy import create_engine

from src.core.config.config import Config

engine = create_engine(Config.DATABASE_URI)
