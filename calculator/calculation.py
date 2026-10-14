from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(cls, a, b, operation):
        return cls(a, b, operation)

    @abstractmethod
    def execute(self):  # pragma: no cover
        pass


class ArithmeticCalculation(Calculation):
    def execute(self):
        return self.operation(self.a, self.b)

