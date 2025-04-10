from strategies.base_strategy import BaseStrategy
import numpy as np

class BackpropStrategy(BaseStrategy):
    def __init__(self, num_arms, lr=0.01):
        self.num_arms = num_arms
        self.mu = np.zeros(num_arms)
        self.lr = lr
        self.counts = np.zeros(num_arms)

    def select_arm(self):
        return np.argmax(self.mu)

    def update(self, arm_index, reward):
        error = reward - self.mu[arm_index]
        gradient = -error  # loss = (reward - mu)^2 -> dL/dmu = -2 * error
        self.mu[arm_index] -= self.lr * gradient
        self.counts[arm_index] += 1