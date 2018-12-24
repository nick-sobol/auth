from marshmallow import (Schema, fields, validate, validates_schema, post_load)
from exceptions import AuthenticationForbidden

from database import session_factory
from .models import User


class AuthSchema(Schema):
    username = fields.String(required=True,
                             validate=validate.Regexp('^[a-zA-Z]{3,}$'),
                             error=AuthenticationForbidden)

    password = fields.String(required=True, validate=validate.Regexp(
        "^[A-Za-z\d@$!%*#?&]{8,}$"
    ))


    confirm_password = fields.String()

    # @validate('username')
    # def test(self, username):
    #     if validate.Regexp('^[a-zA-Z]{3,}$'):
    #
    # @validates_schema
    # def validate_match(self, data):
    #
    #     if data.get('password') != data.get('confirm_password'):
    #         raise AuthenticationForbidden('Passwords must be the same')
    #
    #     return True


auth_schema = AuthSchema(strict=True)