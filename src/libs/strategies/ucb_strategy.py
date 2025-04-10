import numpy as np
from .base_strategy import BaseStrategy

class UCBStrategy(BaseStrategy):
    def __init__(self, num_arms):
        self.counts = np.zeros(num_arms)
        self.values = np.zeros(num_arms)
        self.total_count = 0

    def select_arm(self):
        self.total_count += 1
        if 0 in self.counts:
            return np.argmin(self.counts)
        ucb_values = self.values + np.sqrt(2 * np.log(self.total_count) / self.counts)
        return np.argmax(ucb_values)

    def update(self, arm_index, reward):
        self.counts[arm_index] += 1
        n = self.counts[arm_index]
        self.values[arm_index] += (reward - self.values[arm_index]) / n
