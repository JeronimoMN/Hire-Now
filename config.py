import os

DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "hirenow.sqlite"
)

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_FILE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'NOT-SECRET-KEY' #Sesiones

class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testhirenow.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'NOT-SECRET-KEY'  # Sesiones
    TESTING = True