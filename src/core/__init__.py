from .config import db_session, engine
from .models import *

# This defines the import orden of the database models, it represents
# the order of table creation on the database.
# This is VERY important to ensure consistency on data creation
