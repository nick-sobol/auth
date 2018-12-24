from os import environ
from os.path import join, dirname
from sanic_jinja2 import SanicJinja2
from dotenv import load_dotenv


envpath = join(dirname(__file__), '.env')
load_dotenv(envpath)


JINJA = SanicJinja2()
SECRET_KEY = environ.get('SECRET_KEY')
DB_URL = environ.get('DB_URL')


__all__ = ['JINJA', 'DB_URL', 'SECRET_KEY']