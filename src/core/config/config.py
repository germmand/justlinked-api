import os

class Config(object):
    DATABASE_URI = "sqlite:///justlinked.db"
    DEBUG = True
    TESTING = True
    HOST = 'http://localhost:8080'
    WEBCLIENT_HOST = 'http://localhost'
    GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
    GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]

class DevelopmentConfig(Config):
    DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///justlinked.db")
    HOST = 'http://localhost:8000'
    WEBCLIENT_HOST = 'http://localhost:4200'

class StagingConfig(Config):
    DATABASE_URI = os.environ["DATABASE_URL"]
    HOST = 'http://localhost:5000'
    WEBCLIENT_HOST = os.getenv('WEBCLIENT_HOST', 'http://localhost')

class ProductionConfig(Config):
    DATABASE_URI = os.environ["DATABASE_URL"]
    DEBUG = False
    TESTING = False
    HOST = 'https://justlinked-api2.herokuapp.com'
    WEBCLIENT_HOST = 'https://justlinked-app.netlify.com'

def get_config():
    config_env = os.getenv('JUSTLINKED_ENV', 'development').lower()
    config_switcher = {
        'development': DevelopmentConfig(),
        'staging': StagingConfig(),
        'production': ProductionConfig()
    }
    return config_switcher[config_env]

Config = get_config()