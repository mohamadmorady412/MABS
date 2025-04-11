from factories.exeptions import NotImplementedInSystem
from strategies.base_strategy import BaseStrategy

class StrategyFactory:
    _registry = {}

    @classmethod
    def register(cls, key: str, strategy_cls: type):
        cls._registry[key] = strategy_cls

    @classmethod
    def create(cls, config: dict, **kwargs) -> BaseStrategy:
        strategy_type = config["type"]
        if strategy_type not in cls._registry:
            raise NotImplementedInSystem("Strategy", strategy_type)
        return cls._registry[strategy_type](**kwargs)
