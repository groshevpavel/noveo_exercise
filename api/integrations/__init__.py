from abc import abstractmethod, ABCMeta
from datetime import datetime


class NotificationClientBase(metaclass=ABCMeta):
    name_ = None

    @abstractmethod
    def notify(self, notification_data: str) -> None:
        pass

    @property
    def id(self):
        if self.name_ is None:
            raise ValueError('NotificationClient need to set it\'s name_ property')
        return f'{self.name_}-{datetime.now().timestamp()}'
