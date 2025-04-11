from factories.bandit_factory import BanditFactory
from factories.strategy_factory import StrategyFactory
from factories.exeptions import NotImplementedInSystem

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
    logger.info(f"{strategy_type} on {bandit_type}: Average Reward = {avg_reward:.3f}")

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Run bandit experiment.")
    parser.add_argument("--bandit", required=True, help="Type of bandit to use")
    parser.add_argument("--strategy", required=True, help="Type of strategy to use")
    parser.add_argument("--arms", type=int, default=10, help="Number of arms")
    parser.add_argument("--trials", type=int, default=1000, help="Number of trials")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    try:
        run_experiment(args.bandit, args.strategy, args.arms, args.trials)
    except NotImplementedInSystem as e:
        logger.error(f"[ERROR] {e}")
