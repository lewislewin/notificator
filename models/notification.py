import os

class Notification():
    def __init__(self, id, source, title, message, priority, organisation):
        self.id = id
        self.source = source
        self.title = title
        self.message = message
        self.priority = priority
        self.link = os.getenv('ZENDESK_TICKET_URL') + str(id)
        self.alert = 'Test Alert'
        self.organisation = organisation

    def __str__(self):
        return f'Notification {self.id}: {self.title}'
        