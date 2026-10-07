class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, operation):
        result = operation.execute()
        self.history.append(operation)
        return result
