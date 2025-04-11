from factories.bandit_factory import BanditFactory
from bandits.base_bandit import BaseBandit

@BanditFactory.register("dummy_bandit")
class DummyBandit(BaseBandit):
    def __init__(self, num_arms):
        self.num_arms = num_arms

    def pull(self, arm):
        return 1.0

def test_register_and_create_bandit():
    config = {"type": "dummy_bandit", "params": {"num_arms": 5}}
    bandit = BanditFactory.create(config)

    assert isinstance(bandit, DummyBandit)
    assert bandit.num_arms == 5
