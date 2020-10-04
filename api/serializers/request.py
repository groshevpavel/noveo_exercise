from datetime import datetime

from marshmallow import Schema, fields, validate, post_load

from api.integrations.recepients import allowed_notification_recipients, NotificationRecipients


class NotifyMessageSchema(Schema):
    text = fields.String(
        required=True, validate=lambda value: len(value) > 0, allow_none=False,
        description='Notify message text',
    )
    recipients = fields.List(
        fields.String, required=True, allow_none=False, validate=validate.ContainsOnly(allowed_notification_recipients),
        description='List of notification handler names',
    )

    @post_load
    def remap_recipients_to_notificators(self, obj):
        recipients = obj.pop('recipients')
        obj['recipients'] = [getattr(NotificationRecipients, recipient).value for recipient in recipients]
        return obj


class NotificationRequestSchema(Schema):
    messages = fields.List(
        fields.Nested(NotifyMessageSchema),
        required=True, allow_none=False, description='Notify message',
    )
    date = fields.DateTime(default=datetime.now)
    sender = fields.String(required=True, allow_none=False)


notification_request = NotificationRequestSchema(strict=True)
