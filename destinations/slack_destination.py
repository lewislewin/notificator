from .abstract_destination import AbstractDestination
from models.notifications.ticket_notification import TicketNotification
import os
import requests


class SlackDestination(AbstractDestination):
    def __init__(self):
        
        pass

    def send_notification(self, ticket: TicketNotification):
        slack_url = os.environ.get('SLACK_URL')
        slack_message = ticket.formatMessageForSlack()

        response = requests.post(slack_url, json={'text': slack_message})

        if response.status_code != 200:
            raise ValueError(
                f'Request to Slack returned an error {response.status_code}, {response.text}'
            )
        
        return True
    
    