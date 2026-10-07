from calculator.operations import Add, Subtract
from calculator.calculator import Calculator


def test_add():

    addition = Add(10, 5)

    assert addition.execute() == 15


def test_add_negative_numbers():

    addition = Add(-10, -5)

    assert addition.execute() == -15


def test_subtract():

    subtraction = Subtract(10, 5)

    assert subtraction.execute() == 5


def test_calculator_history():

    calculator = Calculator()
    addition = Add(10, 5)

    assert calculator.calculate(addition) == 15
    assert calculator.get_history() == [addition]


def test_calculator_history_multiple():

    calculator = Calculator()

    addition = Add(10, 5)
    subtraction = Subtract(10, 3)

    calculator.calculate(addition)
    calculator.calculate(subtraction)

    assert calculator.get_history() == [addition, subtraction]

def test_history_is_encapsulated():
    calculator = Calculator()

    assert not hasattr(calculator, "history")
    assert hasattr(calculator, "_history")

def test_calculator_history_starts_empty():
    calculator = Calculator()

    assert calculator.get_history() == []
