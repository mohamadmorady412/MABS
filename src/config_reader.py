import yaml
from pathlib import Path

config_path = Path("../config/config.yaml")

def load_config():
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    
    return config
