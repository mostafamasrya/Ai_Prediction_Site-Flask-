from ast import Or
import os

class Config:
    
    """ basic configurations."""
    DEBUG = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('ENV')
    FLASK_APP = os.environ.get('APP_NAME')
    # SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres:123456@localhost/aiproject"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class development(Config):
    """development configuration """
    DEBUG = True 

class production(Config):
    """ production configuration """
    PORT = os.environ.get('PORT') or 8080
