from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def run():
    history = []

    strategies = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    while True:
        try:
            user_input = input("> ").strip()

            if user_input == "exit":
                break

            if user_input == "history":
                past_calculations = HistoryCommand(history).execute()

                if not past_calculations:
                    print("No calculations yet.")
                else:
                    for calculation in past_calculations:
                        print(
                            calculation.a,
                            calculation.operation.__name__,
                            calculation.b,
                        )
                continue

            parts = user_input.split()

            if len(parts) != 3:
                print("Error: Enter a command and two numbers.")
                continue

            command_name = parts[0]

            if command_name not in strategies:
                print("Error: Unknown command.")
                continue

            try:
                a = float(parts[1])
                b = float(parts[2])
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue

            try:
                calculation = ArithmeticCalculation.create(
                    a, b, strategies[command_name]
                )
                result = CalculateCommand(calculation, history).execute()
                print(result)
            except ValueError as error:
                print(f"Error: {error}")

        except EOFError:
            break
