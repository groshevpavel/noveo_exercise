import logging

from api.integrations import NotificationClientBase


class LogNotificationClient(NotificationClientBase):
    name_ = 'LOGGER'

    def notify(self, notification_data: str):
        print(f'Call {self.name_} notification gate with text: "{notification_data}"')
        return self.id
