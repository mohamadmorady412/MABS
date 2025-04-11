from factories.exeptions import NotImplementedInSystem

from experiment import run_experiment
from logger import get_logger
from utils.auto_import import import_modules_from_folder


import_modules_from_folder("bandits", "bandits")
import_modules_from_folder("strategies", "strategies")

logger = get_logger(__name__)

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
