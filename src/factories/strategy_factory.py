class StrategyFactory:
    registry = {}

    @classmethod
    def register(cls, name):
        def decorator(subclass):
            cls.registry[name] = subclass
            return subclass
        return decorator

    @classmethod
    def create(cls, config: dict, num_arms):
        strategy_type = config["type"]
        if strategy_type not in cls.registry:
            raise ValueError(f"Unknown strategy type: {strategy_type}")
        return cls.registry[strategy_type](num_arms=num_arms)