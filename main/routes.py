import flask

from main.serializers.notify import notification_request

main_blueprint = flask.Blueprint('main', __name__)


@main_blueprint.route("/notify", methods=["POST"])
def notify():
    notification_data = notification_request.load(flask.request.json).data
    return notification_data
