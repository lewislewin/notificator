import os
from models.notifications.abstract_notification import AbstractNotification

class TicketNotification(AbstractNotification):
    class Ticket:
        id = None
        title = None
        description = None
        priority = None
        organisation = None
        link = None
    class Alert:
        notificationGroup = '!here'
        title = None

    alert = Alert()
    ticket = Ticket()

    def __init__(self, ticketId, ticketTitle, ticketDescription, ticketPriority, ticketOrganization, alertTitle, notificationGroup):
        self.ticket.id = ticketId
        self.ticket.title = ticketTitle
        self.ticket.description = ticketDescription
        self.ticket.priority = ticketPriority
        self.ticket.organisation = ticketOrganization
        self.setLink(ticketId=ticketId)

        if alertTitle is not None:
            self.alert.title = alertTitle
        
        if notificationGroup is not None:
            self.alert.notificationGroup = notificationGroup


    def formatMessageForSlack(self) -> str:

        formattedMessage = f'Alert <{self.alert.notificationGroup}>: {self.alert.title} \r\n'
        formattedMessage += f' <{self.ticket.link}|{self.ticket.id}> | {self.ticket.title} - {self.ticket.organisation}\r\n'

        return formattedMessage
    
    def setLink(self, ticketId):
        self.ticket.link = f'{os.getenv("ZENDESK_TICKET_URL")}/agent/tickets/{ticketId}'
    