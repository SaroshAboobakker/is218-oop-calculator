class CalculateCommand:
    def __init__(self, calculation, history):
        self.calculation = calculation
        self.history = history

    def execute(self):
        result = self.calculation.execute()
        self.history.append(self.calculation)
        return result


class HistoryCommand:
    def __init__(self, history):
        self.history = history

    def execute(self):
        return self.history.copy()
