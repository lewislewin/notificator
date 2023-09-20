from .abstract_destination import AbstractDestination
from models.notification import Notification
import os
import requests


class SlackDestination(AbstractDestination):
    def __init__(self):
        
        pass

    def send_notification(self, notification: Notification):
        slack_url = os.environ.get('SLACK_URL')
        slack_message = self.format_message(notification)

        response = requests.post(slack_url, json={'text': slack_message})

        if response.status_code != 200:
            raise ValueError(
                f'Request to Slack returned an error {response.status_code}, {response.text}'
            )
        
        return True
    
    def format_message(self, notification: Notification) -> str:
        formatted_message = f'Alert <!here>: {notification.alert} \r\n'
        formatted_message += f' <{notification.link}|{notification.id}> | {notification.title} - {notification.organisation}\r\n'

        return formatted_message
    