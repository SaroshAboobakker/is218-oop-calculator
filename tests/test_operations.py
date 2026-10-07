from calculator.operations import Add, Subtract


def test_add():
    addition = Add(10, 5)
    assert addition.execute() == 15


def test_add_negative_numbers():
    addition = Add(-10, -5)
    assert addition.execute() == -15
def test_subtract():
    subtraction = Subtract(10, 5)
    assert subtraction.execute() == 5
