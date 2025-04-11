from factories.strategy_factory import StrategyFactory
from strategies.base_strategy import BaseStrategy

@StrategyFactory.register("dummy_strategy")
class DummyStrategy(BaseStrategy):
    def __init__(self, num_arms):
        self.num_arms = num_arms

    def select_arm(self):
        return 0

    def update(self, arm, reward):
        pass

def test_register_and_create_strategy():
    config = {"type": "dummy_strategy"}
    strategy = StrategyFactory.create(config, num_arms=10)

    assert isinstance(strategy, DummyStrategy)
    assert strategy.num_arms == 10
