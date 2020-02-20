from graphene_sqlalchemy import SQLAlchemyConnectionField

from src.positions.schema.types import PositionType

all_positions = SQLAlchemyConnectionField(PositionType)
