from os import environ
from sanic_jinja2 import SanicJinja2, Environment, PackageLoader
from dotenv import load_dotenv
from os.path import join, dirname


class Settings:

    def __init__(self, filename='.env'):
        envpath = join(dirname(__file__), filename)
        load_dotenv(envpath)

        self.SECRET_KEY = environ.get('SECRET_KEY')

        self.templates_env = Environment(
            loader=PackageLoader('apps', 'templates')
        )

        self.jinja = SanicJinja2()


settings = Settings()
