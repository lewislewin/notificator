from abc import ABC, abstractmethod

class AbstractSource(ABC):
    @abstractmethod
    def handle_webhook(self, request):
        pass

    @abstractmethod
    def verify_request(self, request):
        pass
