from factories.bandit_factory import BanditFactory
from bandits.base_bandit import BaseBandit
import numpy as np

@BanditFactory.register("random")
class RandomBandit(BaseBandit):
    def __init__(self, num_arms):
        self.num_arms = num_arms

    def pull(self, arm):
        return np.random.rand()
