from factories.exeptions import NotImplementedInSystem
from bandits.base_bandit import BaseBandit
class BanditFactory:
    _registry = {}

    @classmethod
    def register(cls, key: str):
        def decorator(bandit_cls):
            cls._registry[key] = bandit_cls
            return bandit_cls
        return decorator

    @classmethod
    def create(cls, config: dict) -> BaseBandit:
        bandit_type = config["type"]
        params = config.get("params", {})
        if bandit_type not in cls._registry:
            raise NotImplementedInSystem("Bandit", bandit_type)
        return cls._registry[bandit_type](**params)
