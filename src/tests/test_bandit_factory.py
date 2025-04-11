import pytest
from factories.bandit_factory import BanditFactory
from factories.exeptions import NotImplementedInSystem

def test_bandit_not_implemented():
    fake_config = {
        "type": "non_existent_bandit",
        "params": {"num_arms": 5}
    }

    with pytest.raises(NotImplementedInSystem) as exc_info:
        BanditFactory.create(fake_config)

    assert "Bandit 'non_existent_bandit' is not implemented" in str(exc_info.value)
