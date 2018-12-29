from database import get_engine
from exceptions import BadRequest, Forbidden
from hash import hash_password
from sanic.exceptions import NotFound

from .serializers import login_schema, register_schema
from .models import User


async def authenticate(request, *args, **kwargs):
    userdata = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
        'confirm_password': request.form.get('confirm_password'),
    }

    if request.form.get('register_enabled'):
        register_schema.load(userdata)

        db_user = await User.get_user(userdata['username'])

        if db_user:
            raise Forbidden({
                'username': 'User with such username already exists',
            })

        engine = await get_engine()

        async with engine.acquire() as conn:
            await conn.execute(
                User.insert().values(
                    username=userdata['username'],
                    password=hash_password(userdata['password'])
                )
            )

        return await User.get_user(userdata['username'])

    else:
        login_schema.load(userdata)

        db_user = await User.get_user(userdata['username'])

        if not db_user:
            raise NotFound({
                'username': 'User with such username does not exist',
            })
        if hash_password(userdata['password']) != db_user['password']:
            raise BadRequest({
                'password': 'User entered incorrect password',
            })

        return db_user

