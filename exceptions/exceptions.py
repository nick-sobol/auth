from sanic.exceptions import SanicException


class Forbidden(SanicException):
    status_code = 403


class ValidationError(SanicException):
    status_code = 422
