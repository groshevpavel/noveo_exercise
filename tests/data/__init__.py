import json
import os


def open_file(filename):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r', encoding='utf-8') as f:
        return json.load(f)


notify_request_data = open_file('notify_request_data.json')
