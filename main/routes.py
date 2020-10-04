import flask

from main.controllers.notifications import notify_all
from main.serializers.request import notification_request
from main.serializers.response import notification_response

main_blueprint = flask.Blueprint('main', __name__)


@main_blueprint.route("/notify", methods=["POST"])
def notify():
    notification_data = notification_request.load(flask.request.json).data
    notification_report = notify_all(notification_data)
    result = notification_response.dump(notification_report).data
    return flask.jsonify(result)
