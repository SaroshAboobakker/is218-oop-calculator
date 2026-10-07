class Operation:
    def execute(self):
        raise NotImplementedError


class Add(Operation):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def execute(self):
        return self.first + self.second
class Subtract(Operation):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def execute(self):
        return self.first - self.second
