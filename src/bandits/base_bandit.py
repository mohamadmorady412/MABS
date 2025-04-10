from abc import ABC, abstractmethod

class BaseBandit(ABC):
    @abstractmethod
    def pull(self, arm):
        pass