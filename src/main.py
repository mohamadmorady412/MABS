from config_reader import load_config


config = load_config()
print(f"{config["Try"]["NUM_TRIALS"]}")