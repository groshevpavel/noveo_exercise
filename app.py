import flask

from main.routes import main_blueprint


def create_app() -> flask.Flask:

    app = flask.Flask(__name__)

    app.url_map.strict_slashes = False

    app.register_blueprint(main_blueprint)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, port=8080)
