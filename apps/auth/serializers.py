from marshmallow import Schema, fields, validates_schema, validate

from exceptions import ValidationError


class LoginSchema(Schema):
    username = fields.String(required=True,
                             validate=validate.Regexp('^[a-zA-Z]{4,32}$'))
    password = fields.String(
        required=True,
        validate=validate.Regexp(
            "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,12}$"
        )
    )

    def handle_error(self, exc, data):
        raise ValidationError(f'{exc}')


class RegisterSchema(LoginSchema):

    confirm_password = fields.String(required=True)

    @validates_schema(skip_on_field_errors=True)
    def validate_match(self, data):

        if data.get('password') != data.get('confirm_password'):
            raise ValidationError({
                'password': 'Entered user passwords must be the same',
            })


login_schema = LoginSchema(strict=True)
register_schema = RegisterSchema(strict=True)
