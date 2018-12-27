from marshmallow import (Schema, fields, validates_schema, validate,
                         post_load)

from exceptions import BadRequest, Forbidden
from database import session_factory
from hash import hash_password
from .models import User


class AuthScheme(Schema):
    username = fields.String(required=True,
                             validate=validate.Regexp('^[a-zA-Z]{4,32}$'))
    password = fields.String(
        required=True,
        validate=validate.Regexp(
            "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        )
    )


class LoginSchema(AuthScheme):

    @post_load
    def get_user_instance(self, data):
        db_user = User.get_user(data)

        if db_user and hash_password(data['password']) != db_user.password:
            raise BadRequest('User entered password do not match')

        return db_user


class RegisterSchema(AuthScheme):

    confirm_password = fields.String(required=True)

    @validates_schema(skip_on_field_errors=True)
    def validate_match(self, data):

        if data.get('password') != data.get('confirm_password'):
            raise BadRequest('Entered user passwords must be the same')

    @post_load
    def register_user(self, data):
        session = session_factory()

        if User.get_user(data, session):
            raise Forbidden('User with such username already exists')

        user = User(username=data['username'],
                    password=hash_password(data['password']))

        session.add(user)
        session.commit()

        return user


login_schema = LoginSchema()
register_schema = RegisterSchema()
