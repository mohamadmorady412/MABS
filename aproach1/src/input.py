# Copyright 2025 Mohammadjavad Morady

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Prompts the user to enter and validates the bandit type and strategy.
==============================================================
example:
>>> user_selection = get_validated_bandit_strategy_input()
>>> print(f"User selection: {user_selection}")
>>> selected_bandit = user_selection.get('bandit')
>>> selected_strategy = user_selection.get('strategy')

>>> if selected_bandit:
>>>    print(f"Selected bandit type: {selected_bandit}")
>>> if selected_strategy:
>>>    print(f"Selected strategy: {selected_strategy}")
==============================================================
"""

from typing import Dict, Optional
from enum import Enum
from logger import get_logger

class BanditType(Enum):
    BERNOULLI_BANDIT = "bernoulli_bandit"
    GAUSSIAN_BANDIT = "gaussian_bandit"

class StrategyType(Enum):
    EPSILON_GREEDY_STRATEGY = "epsilon_greedy_strategy"
    GREEDY_STRATEGY = "greedy_strategy"
    RANDOM_STRATEGY = "random_strategy"
    THOMPSON_SAMPLING_STRATEGY = "thompson_sampling_strategy"
    UCB_STRATEGY = "ucb_strategy"

log = get_logger(__name__)

def get_validated_bandit_strategy_input() -> Dict[str, Optional[str]]:
    """
    Prompts the user to enter and validates the bandit type and strategy.

    Returns:
        A dictionary containing the validated 'bandit' and 'strategy' values.
    """
    problem: Dict[str, Optional[str]] = {}

    for input_type, EnumClass, prompt in [
        ('bandit', BanditType, f"Please enter the bandit type from ({', '.join([b.value for b in BanditType])}): "),
        ('strategy', StrategyType, f"Please enter the strategy from ({', '.join([s.value for s in StrategyType])}): ")
    ]:
        while problem.get(input_type) is None:
            user_input = input(prompt).strip().lower()
            try:
                member = EnumClass(user_input)
                problem[input_type] = member.value
            except ValueError:
                log.error(f"The entered {input_type} '{user_input}' is invalid. Please choose from the list above.")

    log.info(f"User chose -> bandit:{problem.get('bandit')} and strategy:{problem.get('strategy')}")
    return problem
