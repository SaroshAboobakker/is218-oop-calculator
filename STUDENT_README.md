# IS218 OOP Calculator

## Project Overview

This project is a command-line calculator built with Python and object-oriented programming. It supports addition, subtraction, multiplication, and division. It also stores calculation history during the current session.

## Requirements

- Python 3.12 or newer
- pip

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Calculator

From the project root, run:

```bash
python -m calculator
```

Example session:

```text
> add 5 3
8.0

> divide 6 3
2.0

> history
5.0 add 3.0
6.0 divide 3.0

> exit
```

Available commands include `add`, `subtract`, `multiply`, `divide`, `history`, and `exit`. Division by zero produces an error instead of crashing the calculator.

## Run the Tests

Run the tests with the required 100% line coverage:

```bash
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

The tests check the arithmetic operations, calculation factory, command classes, command-line behavior, and error handling.

The abstract `Calculation.execute` method uses `# pragma: no cover` because it is an abstract placeholder that concrete classes implement. The entry-point guard is also excluded from coverage where applicable because it is only used when the module is run directly. These exclusions should be kept limited to code that cannot meaningfully be tested as ordinary executable behavior.

## Object-Oriented Programming

- **Encapsulation:** Calculation data and related behavior are grouped into classes.
- **Abstraction:** `Calculation` defines a common interface for calculations.
- **Inheritance:** `ArithmeticCalculation` inherits from `Calculation`.
- **Polymorphism:** Concrete calculation objects implement the `execute` method.

## SOLID Principles

- **Single Responsibility:** Operations, calculations, commands, and CLI behavior are separated into different modules.
- **Open/Closed:** New calculation behavior can be added without rewriting the entire CLI.
- **Liskov Substitution:** Concrete calculation classes follow the interface defined by the base class.
- **Interface Segregation:** The calculation interface stays focused on executing a calculation.
- **Dependency Inversion:** The calculator uses operation callables rather than hard-coding each arithmetic formula into the calculation class.

## Design Patterns

- **Factory Method:** `ArithmeticCalculation.create()` creates a calculation object.
- **Command:** `CalculateCommand` and `HistoryCommand` encapsulate user actions.
- **Strategy:** The CLI maps operation names to interchangeable operation functions.

## Static, Class, and Instance Methods

- **Static methods** perform arithmetic without needing an object instance.
- **Class methods** such as `create()` are called on a class and create calculation objects.
- **Instance methods** such as `execute()` operate on an individual calculation.

## GitHub Actions

The GitHub Actions workflow runs the tests when changes are pushed or a pull request is opened.

Workflow page: https://github.com/SaroshAboobakker/is218-oop-calculator/actions

After the workflow succeeds, add a link to the specific successful Actions run here.

