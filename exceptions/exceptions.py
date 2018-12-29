from sanic.exceptions import SanicException


class Forbidden(SanicException):
    status_code = 403


class BadRequest(SanicException):
    status_code = 400
