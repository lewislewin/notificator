from .abstract_source import AbstractSource
from models.notification import Notification

class ZendeskSource(AbstractSource):
    def process_data(self, request) -> Notification:
        data = request['ticket']
        return Notification(
            id = data['id'],
            source = 'Zendesk',
            title = data['title'],
            message = data['description'],
            priority = data['priority'],
            organisation = data['organisation']
        )

    def verify_request(self, request):
        pass