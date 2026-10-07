from calculator.repl import run


def test_invalid_add_input(monkeypatch, capsys):

    inputs = iter(["add", "hello", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Please enter numbers only." in output


def test_invalid_subtract_input(monkeypatch, capsys):

    inputs = iter(["subtract", "hello", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Please enter numbers only." in output


def test_help_command(monkeypatch, capsys):

    inputs = iter(["help", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Commands: add, subtract, history, help, exit" in output


def test_history_command(monkeypatch, capsys):

    inputs = iter(["add", "10", "5", "history", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Add 10.0 5.0" in output


def test_subtract_command(monkeypatch, capsys):

    inputs = iter(["subtract", "10", "3", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "7.0" in output


def test_repl_main(monkeypatch):

    inputs = iter(["exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import runpy

    runpy.run_module("calculator.repl", run_name="__main__")
