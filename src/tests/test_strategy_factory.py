import pytest
from factories.strategy_factory import StrategyFactory
from factories.exeptions import NotImplementedInSystem

def test_strategy_not_implemented():
    fake_config = {
        "type": "ghost_strategy"
    }

    with pytest.raises(NotImplementedInSystem) as exc_info:
        StrategyFactory.create(fake_config, num_arms=5)

    assert "Strategy 'ghost_strategy' is not implemented" in str(exc_info.value)
