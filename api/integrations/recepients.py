from enum import Enum

from api.integrations import NotificationClientBase
from api.integrations.email.client import EmailNotificationClient
from api.integrations.http.client import HTTPNotificationClient
from api.integrations.logging.client import LogNotificationClient
from api.integrations.slack.client import SlackNotificationClient
from api.integrations.sms.client import SmsNotificationClient


class NotificationRecipients(Enum):
    LOG: NotificationClientBase = LogNotificationClient
    SMS: NotificationClientBase = SmsNotificationClient
    EMAIL: NotificationClientBase = EmailNotificationClient
    HTTP: NotificationClientBase = HTTPNotificationClient
    SLACK: NotificationClientBase = SlackNotificationClient


allowed_notification_recipients = [a.name for a in NotificationRecipients]