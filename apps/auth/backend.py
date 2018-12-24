from sanic_jwt import exceptions
from .serializers import auth_schema


async def authenticate(request, *args, **kwargs):
    userdata = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
    }

    user, errors = auth_schema.load(userdata)

    if errors:
        raise exceptions.AuthenticationFailed('Missing username or password')

    return dict(user_id=3)
