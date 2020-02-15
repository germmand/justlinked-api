import os

try:
    DATABASE_URI = os.environ["JUSTLINKED_DB"]
except KeyError:
    print("Environment variable: 'JUSTLINKED_DB' not set, SQLite used instead")
    DATABASE_URI = 'sqlite:///justlinked.db'
