from api.integrations import NotificationClientBase


class EmailNotificationClient(NotificationClientBase):
    name_ = 'EMAIL'

    def notify(self, notification_data: str):
        print(f'Call {self.name_} notification gate with text: "{notification_data}"')
        return self.id
