from os import environ
from os.path import join, dirname
from sanic_jinja2 import SanicJinja2
from dotenv import load_dotenv


envpath = join(dirname(__file__), '.env')
load_dotenv(envpath)

DB_USER = environ.get('POSTGRES_USER')
DB_PASSWORD = environ.get('POSTGRES_PASSWORD')
DB_NAME = environ.get('POSTGRES_DB')
DB_PORT = environ.get('POSTGRES_PORT')
DB_HOST = environ.get('POSTGRES_HOST')
DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

JINJA = SanicJinja2()
SECRET_KEY = environ.get('SECRET_KEY')
SESSION_TIME = 1800
LEEWAY_SESSION_TIME = 25


__all__ = [
    'JINJA', 'DB_URL', 'SECRET_KEY', 'SESSION_TIME', 'LEEWAY_SESSION_TIME',
]