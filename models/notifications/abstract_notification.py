from abc import ABC, abstractmethod
import os

class AbstractNotification(ABC):
    
    @abstractmethod
    def formatMessageForSlack(self) -> str:
        pass
