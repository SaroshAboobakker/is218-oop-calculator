import pytest

from calculator.operations import Operations


def test_add():
    assert Operations.add(5, 3) == 8


def test_add_negative_numbers():
    assert Operations.add(-5, -3) == -8


def test_subtract():
    assert Operations.subtract(5, 3) == 2


def test_multiply():
    assert Operations.multiply(5, 3) == 15


def test_divide():
    assert Operations.divide(6, 3) == 2


def test_divide_decimal():
    assert Operations.divide(5, 3) == pytest.approx(1.6666666667)


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.divide(5, 0)
