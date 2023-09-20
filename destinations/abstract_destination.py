from abc import ABC, abstractmethod

class AbstractDestination(ABC):
    @abstractmethod
    def send_notification(self, request):
        pass