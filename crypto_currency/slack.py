# -*- coding: utf-8 -*-
import json

import requests

from credentials import SLACK_URL, SLACK_ACCESS_TOKEN, SLACK_CHANNEL_ID

def file(channel, file):
    files = {'file': file}
    param = {'token': SLACK_ACCESS_TOKEN, 'channels': SLACK_CHANNEL_ID[channel]}
    requests.post(url="https://slack.com/api/files.upload", params=param, files=files)

def message(channel, message, emoji=':blush:', mention=False):
    message = message + ('\n<!channel>' if mention else '')
    payload = {
        'text': message,
        'icon_emoji': emoji,
    }
    requests.post(SLACK_URL[channel], json.dumps(payload))
