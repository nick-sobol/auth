import config
from sanic import Sanic
from sanic_jwt import Initialize

from apps import jwt_views, home_blueprint
from apps.auth import authenticate


def create_app():
    app = Sanic(__name__)
    Initialize(app, class_views=jwt_views,
               authenticate=authenticate,
               refresh_token_enabled=False,
               cookie_set=True,
               cookie_token_name='access_token',
               secret=config.SECRET_KEY,
               expiration_delta=config.SESSION_TIME,
               leeway=config.LEEWAY_SESSION_TIME)

    app.config.from_object(config)
    config.JINJA.init_app(app)

    app.static('static/', './static/', name='static_home')
    app.static('static/auth', './static/auth', name='static_auth')

    app.blueprint(home_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
