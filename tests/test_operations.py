from calculator.operations import Add


def test_add():
    addition = Add(10, 5)
    assert addition.execute() == 15
