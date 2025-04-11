from factories.bandit_factory import BanditFactory
from factories.strategy_factory import StrategyFactory

from logger import get_logger
from utils.auto_import import import_modules_from_folder

import_modules_from_folder("bandits", "bandits")
import_modules_from_folder("strategies", "strategies")

logger = get_logger(__name__)

def run_experiment(bandit_type, strategy_type, num_arms=10, num_trials=1000):
    bandit = BanditFactory.create({"type": bandit_type, "params": {"num_arms": num_arms}})
    strategy = StrategyFactory.create({"type": strategy_type}, num_arms=num_arms)

    rewards = []
    for _ in range(num_trials):
        arm = strategy.select_arm()
        reward = bandit.pull(arm)
        strategy.update(arm, reward)
        rewards.append(reward)

    avg_reward = sum(rewards) / len(rewards)
    result = f"{strategy_type} on {bandit_type}: Average Reward = {avg_reward:.3f}"
    logger.info(result)
    return result

def run_experiment_as_conf(config: dict):
    bandit_config = config["bandit"]
    strategy_config = config["strategy"]
    num_trials = config["experiment"]["num_trials"]

    bandit = BanditFactory.create(bandit_config)
    strategy = StrategyFactory.create(strategy_config, num_arms=bandit_config["params"]["num_arms"])

    rewards = []
    for _ in range(num_trials):
        arm = strategy.select_arm()
        reward = bandit.pull(arm)
        strategy.update(arm, reward)
        rewards.append(reward)

    avg_reward = sum(rewards) / len(rewards)
    logger.info(f"{strategy_config['type']} on {bandit_config['type']}: Average Reward = {avg_reward:.3f}")
