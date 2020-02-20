import os

try:
    DATABASE_URI = os.environ["DATABASE_URL"]
except KeyError:
    print("Environment variable: 'DATABASE_URL' not set, SQLite used instead")
    DATABASE_URI = 'sqlite:///justlinked.db'
