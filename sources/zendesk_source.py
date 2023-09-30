from .abstract_source import AbstractSource
from models.notifications.ticket_notification import TicketNotification

class ZendeskSource(AbstractSource):
    request = None

    def process_data(self, request) -> TicketNotification:
        self.setRequest(request)
        if not self.checkTicketIsEnterprise() and not self.checkTicketPriority():
            return None
        return self.convertRequestToTicketObject()
    
    def getTicket(self):
        return self.request['ticket']

    def getOrganisation(self):
        return self.request['ticket']['organization']

    def setRequest(self, request):
        #add check for valid request
        self.request = request

    def convertRequestToTicketObject(self):
        ticket = TicketNotification(
            ticketId=self.getTicket()['id'],
            ticketTitle=self.getTicket()['title'],
            ticketDescription=self.getTicket()['description'],
            ticketPriority=self.getTicket()['priority'],
            ticketOrganization=self.getOrganisation()['name'],
            alertTitle='New Urgent / Enterprise Zendesk Ticket',
            notificationGroup='!here'
        )
        return ticket
    
    def verify_request(self, request):
        return super().verify_request(request)
    
    def checkTicketPriority(self):
        return self.getTicket()['priority'] == 'urgent'
    
    def checkTicketIsEnterprise(self):
        return 'enterprise' in self.getTicket()['tags']