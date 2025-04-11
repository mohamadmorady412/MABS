import streamlit as st
import pandas as pd
from factories.bandit_factory import BanditFactory
from factories.strategy_factory import StrategyFactory
from utils.auto_import import import_modules_from_folder

import_modules_from_folder("bandits", "bandits")
import_modules_from_folder("strategies", "strategies")

st.title("Multi-Armed Bandit Simulator")

bandit_type = st.selectbox("Select Bandit Type", ["gaussian", "normal", "random"])
strategy_type = st.selectbox("Select Strategy Type", ["epsilon_greedy", "ucb", "thompson"])
num_arms = st.slider("Number of Arms", 2, 20, 10)
num_trials = st.slider("Number of Trials", 100, 5000, 1000)

if st.button("Run Simulation"):
    bandit = BanditFactory.create({"type": bandit_type, "params": {"num_arms": num_arms}})
    strategy = StrategyFactory.create({"type": strategy_type}, num_arms=num_arms)

    rewards = []
    cumulative_rewards = []
    total = 0

    for t in range(num_trials):
        arm = strategy.select_arm()
        reward = bandit.pull(arm)
        strategy.update(arm, reward)
        rewards.append(reward)
        total += reward
        cumulative_rewards.append(total / (t + 1))

    st.subheader("Reward at Each Time Step")
    st.line_chart(pd.DataFrame({"Reward": rewards}))

    st.subheader("Cumulative Average Reward")
    st.line_chart(pd.DataFrame({"Average Reward": cumulative_rewards}))

    st.success(f"Final Average Reward: {cumulative_rewards[-1]:.3f}")
