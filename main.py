import config
from sanic import Sanic
from sanic_jwt import Initialize

from apps import auth_blueprint, home_blueprint
from apps.auth import authenticate


# Setup Sanic app
app = Sanic(__name__)
Initialize(app, authenticate=authenticate)
app.config.from_object(config)
config.JINJA.init_app(app)


# Setup static files
app.static('static/auth', './static/auth', name='static_auth')


# Install blueprints
app.blueprint(auth_blueprint)
app.blueprint(home_blueprint)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
