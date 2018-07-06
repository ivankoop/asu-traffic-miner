from config import NOTIFICATION_APP_TOKEN
from config import NOTIFICATION_USER_TOKEN
import requests

def push(type,message):

    url = "https://api.pushover.net/1/messages.json"
    payload = {
        'token': NOTIFICATION_APP_TOKEN,
        'user': NOTIFICATION_USER_TOKEN,
        'device': 'ios',
        'title': 'Asu Traffic',
        'message': type + ": " + message,
    }

    requests.post(url, data=payload)
