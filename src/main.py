from .config_reader import NUM_ARMS, NUM_TRIALS, EPSILON
from libs.bandits.bernoulli_bandit import BernoulliBandit
from libs.bandits.gaussian_bandit import GaussianBandit

from libs.strategies.random_strategy import RandomStrategy
from libs.strategies.greedy_strategy import GreedyStrategy
from libs.strategies.epsilon_greedy_strategy import EpsilonGreedyStrategy
from libs.strategies.ucb_strategy import UCBStrategy
from libs.strategies.thompson_sampling_strategy import ThompsonSamplingStrategy

from libs.utils.plot import plot_rewards

def get_bandit(name):
    if name == "bernoulli":
        return BernoulliBandit(NUM_ARMS)
    if name == "gaussian":
        return GaussianBandit(NUM_ARMS)
    raise ValueError("Invalid bandit type")

def get_strategy(name):
    if name == "random":
        return RandomStrategy(NUM_ARMS)
    if name == "greedy":
        return GreedyStrategy(NUM_ARMS)
    if name == "epsilon_greedy":
        return EpsilonGreedyStrategy(NUM_ARMS, EPSILON)
    if name == "ucb":
        return UCBStrategy(NUM_ARMS)
    if name == "thompson":
        return ThompsonSamplingStrategy(NUM_ARMS)
    raise ValueError("Invalid strategy type")

def run(bandit_type, strategy_type):
    bandit = get_bandit(bandit_type)
    strategy = get_strategy(strategy_type)

    cumulative_reward = 0
    rewards = []

    for _ in range(NUM_TRIALS):
        arm = strategy.select_arm()
        reward = bandit.pull(arm)
        strategy.update(arm, reward)
        cumulative_reward += reward
        rewards.append(cumulative_reward)

    print("Total Reward:", cumulative_reward)
    plot_rewards(rewards)

if __name__ == "__main__":
    bandit_input = input("Bandit Type (bernoulli/gaussian): ")
    strategy_input = input("Strategy (random/greedy/epsilon_greedy/ucb/thompson): ")
    run(bandit_input.lower(), strategy_input.lower())
