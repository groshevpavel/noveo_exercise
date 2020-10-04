import pytest

from api.integrations import NotificationClientBase


class BlankNotificationClient(NotificationClientBase):
    pass


class NoNameNotificationClient(NotificationClientBase):
    def notify(self, notification_data: str) -> None:
        pass


def test_notification_client():
    with pytest.raises(TypeError) as e:
        client = BlankNotificationClient()

    assert e.value.args[0] == "Can't instantiate abstract class BlankNotificationClient with abstract methods notify"


def test_notification_client_name():
    with pytest.raises(ValueError) as e:
        client = NoNameNotificationClient()
        id_ = client.id

    assert e.value.args[0] == 'NotificationClient need to set it\'s name_ property'
