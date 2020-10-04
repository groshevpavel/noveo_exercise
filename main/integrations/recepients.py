from enum import Enum

from main.integrations import NotificationClientBase
from main.integrations.email.client import EmailNotificationClient
from main.integrations.http.client import HTTPNotificationClient
from main.integrations.logging.client import LogNotificationClient
from main.integrations.slack.client import SlackNotificationClient
from main.integrations.sms.client import SmsNotificationClient


class NotificationRecipients(Enum):
    LOG: NotificationClientBase = LogNotificationClient
    SMS: NotificationClientBase = SmsNotificationClient
    EMAIL: NotificationClientBase = EmailNotificationClient
    HTTP: NotificationClientBase = HTTPNotificationClient
    SLACK: NotificationClientBase = SlackNotificationClient


allowed_notification_recipients = [a.name for a in NotificationRecipients]