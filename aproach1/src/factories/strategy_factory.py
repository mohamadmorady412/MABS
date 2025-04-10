class StrategyFactory:
    registry = {}

    @classmethod
    def register(cls, name):
        def inner(subclass):
            cls.registry[name] = subclass
            return subclass
        return inner

    @classmethod
    def create(cls, config: dict, num_arms: int):
        strategy_type = config["type"]
        params = config.get("params", {})
        if strategy_type not in cls.registry:
            raise ValueError(f"Unknown strategy type: {strategy_type}")
        return cls.registry[strategy_type](num_arms=num_arms, **params)
