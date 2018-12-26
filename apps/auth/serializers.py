from marshmallow import (Schema, fields, validates_schema, validate,
                         post_load, pre_load)

from exceptions import Forbidden
from database import session_factory
from hash import hash_password
from .models import User


class AuthSchema(Schema):
    username = fields.String(required=True,
                             validate=validate.Regexp('^[a-zA-Z]{4,32}$'))

    password = fields.String(
        required=True,
        validate=validate.Regexp(
            "^[A-Za-z\d@$!%*#?&]{8,}$"
        )
    )

    confirm_password = fields.String(allow_none=True)

    @validates_schema(skip_on_field_errors=True)
    def validate_match(self, data):

        if (data.get('confirm_password') and
                data.get('password') != data.get('confirm_password')):

            raise Forbidden('Entered user passwords must be the same')

    @post_load
    def get_user_instance(self, data):
        session = session_factory()

        confirm_password = data.get('confirm_password')

        user = User(username=data['username'],
                    password=hash_password(data['password']))

        db_user = (
            session.query(User).filter(User.username == user.username).first()
        )

        if db_user and confirm_password:
            raise Forbidden('User with such username already exists')
        elif not db_user and not confirm_password:
            raise Forbidden('User with such username does not exist')
        elif db_user and db_user.password != user.password:
            raise Forbidden('User passwords do not match')

        if not db_user and confirm_password:
            session.add(user)
            session.commit()

        return user


auth_schema = AuthSchema()
