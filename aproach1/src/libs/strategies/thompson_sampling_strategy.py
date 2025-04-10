import numpy as np
from .base_strategy import BaseStrategy

class ThompsonSamplingStrategy(BaseStrategy):
    def __init__(self, num_arms):
        self.successes = np.ones(num_arms)
        self.failures = np.ones(num_arms)

    def select_arm(self):
        samples = np.random.beta(self.successes, self.failures)
        return np.argmax(samples)

    def update(self, arm_index, reward):
        if reward:
            self.successes[arm_index] += 1
        else:
            self.failures[arm_index] += 1
