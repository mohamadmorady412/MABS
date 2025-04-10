import abc

class BaseStrategy(abc.ABC):
    @abc.abstractmethod
    def select_arm(self):
        pass

    @abc.abstractmethod
    def update(self, arm_index, reward):
        pass
