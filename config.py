from os import environ
from sanic_jinja2 import SanicJinja2
from dotenv import load_dotenv
from os.path import join, dirname

envpath = join(dirname(__file__), '.env')
load_dotenv(envpath)


JINJA = SanicJinja2()
SECRET_KEY = environ.get('SECRET_KEY')