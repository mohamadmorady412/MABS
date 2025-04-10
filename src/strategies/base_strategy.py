from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def select_arm(self):
        pass

    @abstractmethod
    def update(self, arm, reward):
        pass