from sanic import Sanic
from apps.auth import auth_blueprint
from settings import settings


# Setup Sanic app
app = Sanic(__name__)
app.config.from_object(settings)
settings.jinja.init_app(app)


# Install blueprints
app.blueprint(auth_blueprint)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)