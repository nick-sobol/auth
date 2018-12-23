from sanic import Sanic
from apps.auth import auth_blueprint
import config

# Setup Sanic app
app = Sanic(__name__)
app.config.from_object(config)
config.JINJA.init_app(app)


# Setup static files
app.static('static/auth', './static/auth', name='static_auth')


# Install blueprints
app.blueprint(auth_blueprint)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
