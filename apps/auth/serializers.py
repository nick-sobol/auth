from marshmallow import Schema, fields


class AuthSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String()


auth_schema = AuthSchema()