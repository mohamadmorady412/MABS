from factories.strategy_factory import StrategyFactory
from strategies.base_strategy import BaseStrategy
import numpy as np

@StrategyFactory.register("thompson")
class ThompsonSamplingStrategy(BaseStrategy):
    def __init__(self, num_arms):
        self.successes = [1] * num_arms
        self.failures = [1] * num_arms

    def select_arm(self):
        samples = [np.random.beta(s, f) for s, f in zip(self.successes, self.failures)]
        return samples.index(max(samples))

    def update(self, arm, reward):
        if reward > 0.5:
            self.successes[arm] += 1
        else:
            self.failures[arm] += 1
