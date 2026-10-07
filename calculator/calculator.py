class Calculator:
    def __init__(self):
        self._history = []

    def calculate(self, operation):
        result = operation.execute()
        self._history.append(operation)
        return result

    def get_history(self):
        return self._history
