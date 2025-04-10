import matplotlib.pyplot as plt

def plot_rewards(rewards):
    plt.plot(rewards)
    plt.xlabel("Trial")
    plt.ylabel("Cumulative Reward")
    plt.grid(True)
    plt.title("Reward Over Time")
    plt.show()
