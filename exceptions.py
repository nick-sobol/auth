from sanic_jwt.exceptions import SanicJWTException


class AuthenticationForbidden(SanicJWTException):
    status_code = 403

