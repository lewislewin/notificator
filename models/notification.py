
class Notification():
    def __init__(self, id, source, title, message, priority):
        self.id = id
        self.source = source
        self.title = title
        self.message = message
        self.priority = priority

    def __str__(self):
        return f'Notification {self.id}: {self.title}'
        