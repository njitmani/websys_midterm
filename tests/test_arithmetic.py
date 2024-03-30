import pytest
from App.strategies.arithmetic_strategies import Addition, Subtraction, Division, Multiplication


def test_add_operation():
    strategy = Addition()
    assert strategy.execute(1, 2) == 3
    assert strategy.execute(-1, -2) == -3
    assert strategy.execute(0, 0) == 0


def test_add_operation_with_invalid_inputs():
    strategy = Addition()
    result = strategy.execute("a", 2)
    assert "Error: Invalid value." in result


def test_subtract_operation():
    strategy = Subtraction()
    assert strategy.execute(5, 3) == 2
    assert strategy.execute(-1, -2) == 1
    assert strategy.execute(0, 0) == 0


def test_add_operation_with_invalid_inputs():
    strategy = Subtraction()
    result = strategy.execute("a", 2)
    assert "Error: Invalid value." in result


def test_multiply_operation():
    strategy = Multiplication()
    assert strategy.execute(2, 3) == 6
    assert strategy.execute(-1, -2) == 2
    assert strategy.execute(0, 10) == 0


def test_multiply_operation_with_invalid_inputs():
    strategy = Multiplication()
    result = strategy.execute("a", 2)
    assert "Error: Invalid value." in result


def test_divide_operation():
    strategy = Division()
    assert strategy.execute(6, 3) == 2
    assert strategy.execute(-4, -2) == 2


def test_divide_operation_by_zero():
    strategy = Division()
    result = strategy.execute(10, 0)
    assert result == "Error: Cannot divide by zero."


def test_divide_operation_with_invalid_inputs():
    strategy = Division()
    result = strategy.execute("a", 2)
    assert "Error: Invalid value." in result