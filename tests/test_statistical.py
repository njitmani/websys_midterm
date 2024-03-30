import pytest
from App.strategies.statistical_strategies import MeanOperation, MedianOperation, StdDevOperation

def test_mean_operation():
    strategy = MeanOperation()
    assert strategy.execute(1, 2, 3, 4, 5) == 3
    assert strategy.execute(1, 1, 1, 1, 1) == 1

def test_median_operation():
    strategy = MedianOperation()
    assert strategy.execute(1, 2, 3, 4, 5) == 3
    assert strategy.execute(1, 2, 3, 4, 5, 6) == 3.5

def test_std_dev_operation():
    strategy = StdDevOperation()
    original_execute = strategy.execute.__wrapped__.__get__(strategy, StdDevOperation)
    assert original_execute(1, 2, 3) == pytest.approx(1)
    with pytest.raises(ValueError):
        original_execute(1)