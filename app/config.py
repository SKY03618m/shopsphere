import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'shopsphere-devops-secret-key-2026')
    DATABASE = os.environ.get('DATABASE_PATH', os.path.join(BASE_DIR, 'instance', 'shopsphere.db'))
    TESTING = False

class TestingConfig(Config):
    TESTING = True
    DATABASE = ':memory:'
