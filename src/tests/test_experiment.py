from experiment import run_experiment
from factories.bandit_factory import BanditFactory
from factories.strategy_factory import StrategyFactory
from bandits.base_bandit import BaseBandit
from strategies.base_strategy import BaseStrategy

@BanditFactory.register("constant")
class ConstantBandit(BaseBandit):
    def __init__(self, num_arms):
        self.num_arms = num_arms

    def pull(self, arm):
        return 1.0  # always returns max reward

@StrategyFactory.register("greedy")
class GreedyStrategy(BaseStrategy):
    def __init__(self, num_arms):
        self.num_arms = num_arms

    def select_arm(self):
        return 0

    def update(self, arm, reward):
        pass

def test_run_experiment_with_dummy_components():
    result = run_experiment("constant", "greedy", num_arms=5, num_trials=100)
    assert "Average Reward = 1.000" in result

def test_run_experiment_with_logging(caplog):
    from experiment import run_experiment

    with caplog.at_level("INFO", logger="expriment"):
        run_experiment("constant", "greedy", num_arms=5, num_trials=100)

    assert "" in caplog.text # TODO
