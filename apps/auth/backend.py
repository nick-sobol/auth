from exceptions import BadRequest

from .serializers import auth_schema


async def authenticate(request, *args, **kwargs):

    userdata = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
        'confirm_password': request.form.get('confirm_password'),
    }

    user, errors = auth_schema.load(userdata)

    if errors:
        raise BadRequest(f'{errors}')

    return user
