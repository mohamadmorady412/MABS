import numpy as np
from .base_strategy import BaseStrategy

class EpsilonGreedyStrategy(BaseStrategy):
    def __init__(self, num_arms, epsilon):
        self.epsilon = epsilon
        self.values = np.zeros(num_arms)
        self.counts = np.zeros(num_arms)

    def select_arm(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(len(self.values))
        return np.argmax(self.values)

    def update(self, arm_index, reward):
        self.counts[arm_index] += 1
        n = self.counts[arm_index]
        self.values[arm_index] += (reward - self.values[arm_index]) / n
