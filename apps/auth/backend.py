from sanic_jwt.exceptions import AuthenticationFailed
from exceptions import AuthenticationForbidden

from .serializers import auth_schema


async def authenticate(request, *args, **kwargs):
    userdata = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
    }

    user, errors = auth_schema.load(userdata)

    if not user:
        raise AuthenticationForbidden(
            'User with such credentials does not exist'
        )

    return user
