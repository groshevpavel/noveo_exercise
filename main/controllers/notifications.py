from collections import defaultdict


def notify_all(notification_data: dict) -> dict:
    messages = notification_data.pop('messages')

    result = []
    for message in messages:
        message_text = message.pop('text')
        message_recipients = message.pop('recipients')

        message_notification_report = defaultdict(list)
        message_notification_report['text'] = message_text

        for recipient in message_recipients:
            notification_id = recipient().notify(message_text)
            message_notification_report['notification_ids'].append(notification_id)

        result.append(message_notification_report)

    return result
