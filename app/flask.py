import flask

from api.routes import main_blueprint
from app.errors import register_marshmallow_error_handlers, register_http_error_handlers


def create_app() -> flask.Flask:

    app = flask.Flask(__name__)

    app.url_map.strict_slashes = False

    app.register_blueprint(main_blueprint)

    with app.app_context():
        register_marshmallow_error_handlers(app)
        register_http_error_handlers(app)

    return app
