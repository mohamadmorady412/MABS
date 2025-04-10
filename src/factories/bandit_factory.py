class BanditFactory:
    registry = {}

    @classmethod
    def register(cls, name):
        def decorator(subclass):
            cls.registry[name] = subclass
            return subclass
        return decorator

    @classmethod
    def create(cls, config: dict):
        bandit_type = config["type"]
        params = config.get("params", {})
        if bandit_type not in cls.registry:
            raise ValueError(f"Unknown bandit type: {bandit_type}")
        return cls.registry[bandit_type](**params)