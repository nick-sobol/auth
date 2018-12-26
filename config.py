from os import environ
from os.path import join, dirname
from sanic_jinja2 import SanicJinja2
from dotenv import load_dotenv


envpath = join(dirname(__file__), '.env')
load_dotenv(envpath)


JINJA = SanicJinja2()
SECRET_KEY = environ.get('SECRET_KEY')
DB_URL = environ.get('DB_URL')
SESSION_TIME = 1800
LEEWAY_SESSION_TIME = 25


__all__ = [
    'JINJA', 'DB_URL', 'SECRET_KEY', 'SESSION_TIME', 'LEEWAY_SESSION_TIME',
]