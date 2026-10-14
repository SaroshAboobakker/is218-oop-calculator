from calculator.cli import run


def test_add_command(monkeypatch, capsys):
    inputs = iter(["add 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "8.0" in capsys.readouterr().out


def test_subtract_command(monkeypatch, capsys):
    inputs = iter(["subtract 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "2.0" in capsys.readouterr().out


def test_multiply_command(monkeypatch, capsys):
    inputs = iter(["multiply 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "15.0" in capsys.readouterr().out


def test_divide_command(monkeypatch, capsys):
    inputs = iter(["divide 6 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "2.0" in capsys.readouterr().out


def test_invalid_command(monkeypatch, capsys):
    inputs = iter(["power 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "Unknown command" in capsys.readouterr().out


def test_invalid_numbers(monkeypatch, capsys):
    inputs = iter(["add hello 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "valid numbers" in capsys.readouterr().out


def test_history(monkeypatch, capsys):
    inputs = iter(["add 5 3", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    output = capsys.readouterr().out
    assert "8.0" in output
    assert "add" in output


def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "Cannot divide by zero" in capsys.readouterr().out


def test_empty_history(monkeypatch, capsys):
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "No calculations yet" in capsys.readouterr().out


def test_wrong_number_of_arguments(monkeypatch, capsys):
    inputs = iter(["add 5", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "two numbers" in capsys.readouterr().out


def test_negative_numbers(monkeypatch, capsys):
    inputs = iter(["add -5 -3", "exit"])
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    run()

    assert "-8.0" in capsys.readouterr().out

def test_end_of_file(monkeypatch):
    def raise_eof(*args):
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)
    run()


def test_calculation_factory():
    from calculator.calculation import Calculation, ArithmeticCalculation

    calculation = ArithmeticCalculation.create(5, 3, lambda a, b: a + b)

    assert calculation.execute() == 8

def test_main_entry_point(monkeypatch):
    import runpy

    monkeypatch.setattr("builtins.input", lambda *args: "exit")
    runpy.run_module("calculator", run_name="__main__")

def test_main_import_does_not_run(monkeypatch):
    import runpy

    runpy.run_module("calculator.__main__", run_name="calculator.__main__")
def test_calculation_is_abstract():
    import pytest
    from calculator.calculation import Calculation, ArithmeticCalculation

    with pytest.raises(TypeError):
        Calculation(5, 3, lambda a, b: a + b)
