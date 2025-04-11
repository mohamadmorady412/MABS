import yaml
import os

BASE_CONFIG_PATH = "src/config"

def load_config(path: str = "src/config/default_config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_profile(profile_name: str):
    path = os.path.join(BASE_CONFIG_PATH, "test", f"{profile_name}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Profile '{profile_name}' not found")
    return load_config(path)

def load_bandit(name: str):
    path = os.path.join(BASE_CONFIG_PATH, "bandit_profiles", f"{name}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Bandit config '{name}' not found")
    return load_config(path)

def load_strategy(name: str):
    path = os.path.join(BASE_CONFIG_PATH, "strategy_profiles", f"{name}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Strategy config '{name}' not found")
    return load_config(path)

def load_components(bandit: str, strategy: str, num_trials: int):
    return {
        "bandit": load_bandit(bandit),
        "strategy": load_strategy(strategy),
        "experiment": {
            "num_trials": num_trials
        }
    }
