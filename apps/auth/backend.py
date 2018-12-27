from exceptions import BadRequest

from .serializers import login_schema, register_schema


async def authenticate(request, *args, **kwargs):
    userdata = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
        'confirm_password': request.form.get('confirm_password'),
    }
    print(bool(request.form))
    user, errors = (
        register_schema.load(userdata) if request.form.get('register_enabled')
        else login_schema.load(userdata)
    )

    if errors:
        raise BadRequest(f'{errors}')

    return user


