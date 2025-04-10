from factories.strategy_factory import StrategyFactory
from strategies.base_strategy import BaseStrategy
import math

@StrategyFactory.register("ucb")
class UCBStrategy(BaseStrategy):
    def __init__(self, num_arms):
        self.counts = [0] * num_arms
        self.values = [0.0] * num_arms
        self.total_counts = 0

    def select_arm(self):
        self.total_counts += 1
        for i, count in enumerate(self.counts):
            if count == 0:
                return i
        ucb_values = [val + math.sqrt(2 * math.log(self.total_counts) / count)
                      for val, count in zip(self.values, self.counts)]
        return ucb_values.index(max(ucb_values))

    def update(self, arm, reward):
        self.counts[arm] += 1
        n = self.counts[arm]
        self.values[arm] += (reward - self.values[arm]) / n
