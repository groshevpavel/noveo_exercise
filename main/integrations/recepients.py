from enum import Enum


class NotificationRecipients(Enum):
    LOG: str = 'LOGGING'
    SMS: str = 'SMS GATE'
    EMAIL: str = 'EMAIL GATE'
    HTTP: str = 'HTTP Notification Gate'
    SLACK: str = 'SLACK'


allowed_notification_recipients = [a.name for a in NotificationRecipients]