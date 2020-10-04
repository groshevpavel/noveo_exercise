import flask

main_blueprint = flask.Blueprint('main', __name__)


@main_blueprint.route("/")
def index():
    return "Flask test app!"
