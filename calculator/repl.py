from calculator.calculator import Calculator
from calculator.operations import Add, Subtract


def run():
    calculator = Calculator()
    print("Calculator started")

    while True:
        command = input("> ")

        if command == "exit":
            break

        if command == "add":
            try:
                first = float(input("First number: "))
                second = float(input("Second number: "))

                operation = Add(first, second)
                result = calculator.calculate(operation)

                print(result)
            except ValueError:
                print("Please enter numbers only.")

        if command == "subtract":
            try:
                first = float(input("First number: "))
                second = float(input("Second number: "))

                operation = Subtract(first, second)
                result = calculator.calculate(operation)

                print(result)
            except ValueError:
                print("Please enter numbers only.")

        if command == "history":
            for operation in calculator.get_history():
                print(type(operation).__name__, operation.first, operation.second)

        if command == "help":
            print("Commands: add, subtract, history, help, exit")


if __name__ == "__main__":
    run()
