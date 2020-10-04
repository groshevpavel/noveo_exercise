from copy import deepcopy

from flask import Response
from flask.testing import FlaskClient

from tests import data
from tests.conftest import isfloat


def test_serializers_fail(client: FlaskClient):
    new_notify_request_data = deepcopy(data.notify_request_data)
    new_notify_request_data['messages'][0]['recipients'].append('SLACK1')

    response: Response = client.post('/notify', json=new_notify_request_data)

    assert response.status_code == 400
    assert response.json == {
        'detail': {
            'messages': {
                '0': {
                    'recipients': ['One or more of the choices you made was not acceptable.']
                }
            }
        },
        'error': 'VALIDATION_ERROR',
        'message': 'VALIDATION_ERROR'
    }


def test_notify_endpoint(client: FlaskClient):
    response: Response = client.post('/notify', json=data.notify_request_data)

    assert response.status_code == 200
    response_body = response.json

    for notification_result in response_body:
        assert notification_result['text'] in ['Notification text #1', 'Notification text #2']

        notification_ids = notification_result.get('notification_ids')
        for notification_id in notification_ids:
            prefix, suffix = notification_id.split('-')

            assert prefix in ['LOGGER', 'HTTP', 'SMS', 'SLACK']
            assert isfloat(suffix)
