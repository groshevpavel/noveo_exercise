from marshmallow import Schema, fields, validate


class NotificationResponseSchema(Schema):
    text = fields.String(required=True, allow_none=False, description='Text which was send to notification client')
    notification_ids = fields.List(fields.String, required=True, allow_none=False, validate=validate.Length(min=1))


notification_response = NotificationResponseSchema(strict=True, many=True)
