from datetime import datetime


class NotificationClientMeta(type):
    name_ = None

    def notify(cls, notification_data: str) -> None:
        raise NotImplemented


class NotificationClientBase(metaclass=NotificationClientMeta):
    @property
    def id(self):
        if self.name_ is None:
            raise ValueError('NotificationClient need to set it\'s name_ property')
        return f'{self.name_}-{datetime.now().timestamp()}'
