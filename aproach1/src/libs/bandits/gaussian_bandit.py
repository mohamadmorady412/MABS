import numpy as np
from .base_bandit import BaseBandit

class GaussianBandit(BaseBandit):
    def __init__(self, num_arms):
        self.means = np.random.randn(num_arms)
        self.stds = np.ones(num_arms)

    def pull(self, arm_index):
        return np.random.normal(self.means[arm_index], self.stds[arm_index])

    def get_true_rewards(self):
        return self.means
