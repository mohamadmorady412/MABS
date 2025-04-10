from factories.bandit_factory import BanditFactory
from factories.strategy_factory import StrategyFactory
from utils.auto_import import import_modules_from_folder

import_modules_from_folder("bandits", "bandits")
import_modules_from_folder("strategies", "strategies")

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
    print(f"{strategy_type} on {bandit_type}: Average Reward = {avg_reward:.3f}")

if __name__ == '__main__':
    run_experiment("gaussian", "epsilon_greedy")
