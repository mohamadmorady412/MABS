import abc

class BaseBandit(abc.ABC):
    @abc.abstractmethod
    def pull(self, arm_index: int) -> float:
        pass

    @abc.abstractmethod
    def get_true_rewards(self):
        pass
