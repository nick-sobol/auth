from sanic_jwt.exceptions import SanicJWTException


class Forbidden(SanicJWTException):
    status_code = 403


class BadRequest(SanicJWTException):
    status_code = 400
