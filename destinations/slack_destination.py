from abstract_destination import AbstractDestination

class SlackDestination(AbstractDestination):
    def send_notification(self, request):
        print('Sending notification to Slack!')
        print(request)
        return True