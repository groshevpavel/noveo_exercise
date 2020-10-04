from datetime import datetime

from marshmallow import Schema, fields, validate

from main.integrations.recepients import allowed_notification_recipients


class NotifyMessageSchema(Schema):
    text = fields.String(
        required=True, validate=lambda value: len(value) > 0, allow_none=False,
        description='Notify message text',
    )
    recipients = fields.List(
        fields.String, required=True, allow_none=False, validate=validate.ContainsOnly(allowed_notification_recipients),
        description='List of notification handler names',
    )


class NotificationRequestSchema(Schema):
    messages = fields.List(
        fields.Nested(NotifyMessageSchema),
        required=True, allow_none=False, description='Notify message',
    )
    date = fields.DateTime(default=datetime.now)
    sender = fields.String(required=True, allow_none=False)


notification_request = NotificationRequestSchema(strict=True)
