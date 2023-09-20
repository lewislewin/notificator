from abc import ABC, abstractmethod

class AbstractSource(ABC):
    @abstractmethod
    def process_data(self, request):
        pass

    @abstractmethod
    def verify_request(self, request):
        pass
