from factories.bandit_factory import BanditFactory
from bandits.base_bandit import BaseBandit
import numpy as np

@BanditFactory.register("normal")
class NormalBandit(BaseBandit):
    def __init__(self, num_arms):
        self.means = np.random.normal(5, 2, num_arms)

    def pull(self, arm):
        return np.random.normal(self.means[arm], 1.0)
