import numpy as np
from .base_bandit import BaseBandit

class BernoulliBandit(BaseBandit):
    def __init__(self, num_arms):
        self.probs = np.random.rand(num_arms)

    def pull(self, arm_index):
        return np.random.rand() < self.probs[arm_index]

    def get_true_rewards(self):
        return self.probs
