import flask
from marshmallow.exceptions import ValidationError


class ErrorType:
    VALIDATION_ERROR = 'VALIDATION_ERROR'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    EXTERNAL_SERVICE_ERROR = 'EXTERNAL_SERVICE_ERROR'
    BAD_REQUEST = 'BAD_REQUEST'
    NOT_FOUND = 'NOT_FOUND'
    EXPIRED_TOKEN = 'EXPIRED_TOKEN'
    BAD_TOKEN = 'BAD_TOKEN'
    ACCESS_DENIED = 'ACCESS_DENIED'


def get_error_response(error: str, message=None, detail=None):
    return flask.jsonify(
        {
            'error': error,
            'message': message,
            'detail': detail,
        }
    )


def register_marshmallow_error_handlers(app):
    @app.errorhandler(ValidationError)
    def validation_error(e):
        return get_error_response(ErrorType.VALIDATION_ERROR, ErrorType.VALIDATION_ERROR, detail=e.messages), 400


def error_handler_factory(code, error_type: str):
    def handle_error(e):
        return get_error_response(error_type, error_type), code

    return handle_error


def register_http_error_handlers(app: flask.Flask):
    errors_config = {
        400: {'error_type': ErrorType.BAD_REQUEST},
        404: {'error_type': ErrorType.NOT_FOUND},
        500: {'error_type': ErrorType.INTERNAL_ERROR},
    }

    for code, param in errors_config.items():
        error_handler = error_handler_factory(code, **param)
        app.errorhandler(code)(error_handler)
