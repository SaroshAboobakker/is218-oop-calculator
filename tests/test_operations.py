from calculator.operations import Add


def test_add():
    addition = Add(10, 5)
    assert addition.execute() == 15


def test_add_negative_numbers():
    addition = Add(-10, -5)
    assert addition.execute() == -15
