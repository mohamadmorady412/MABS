from factories.strategy_factory import StrategyFactory
from strategies.base_strategy import BaseStrategy
import random

@StrategyFactory.register("epsilon_greedy")
class EpsilonGreedyStrategy(BaseStrategy):
    def __init__(self, num_arms, epsilon=0.1):
        self.epsilon = epsilon
        self.counts = [0] * num_arms
        self.values = [0.0] * num_arms

    def select_arm(self):
        if random.random() < self.epsilon:
            return random.randrange(len(self.values))
        return self.values.index(max(self.values))

    def update(self, arm, reward):
        self.counts[arm] += 1
        n = self.counts[arm]
        self.values[arm] += (reward - self.values[arm]) / n
