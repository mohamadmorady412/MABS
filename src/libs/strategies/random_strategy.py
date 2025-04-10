import numpy as np
from .base_strategy import BaseStrategy

class RandomStrategy(BaseStrategy):
    def __init__(self, num_arms):
        self.num_arms = num_arms

    def select_arm(self):
        return np.random.randint(self.num_arms)

    def update(self, arm_index, reward):
        pass
