from abc import ABC, abstractmethod
import math
from app.exceptions import OperationError, ValidationError


class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


class Addition(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtraction(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiplication(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b


class Division(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Division by zero is undefined.")
        return a / b


class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b


class Root(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Root degree cannot be zero.")
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of a negative number is complex.")
        return a ** (1 / b)


class Modulus(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Modulus by zero is undefined.")
        return a % b


class IntegerDivision(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Integer division by zero is undefined.")
        return a // b


class Percentage(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Base percentage value cannot be zero.")
        return (a / b) * 100


class AbsoluteDifference(Operation):
    def execute(self, a: float, b: float) -> float:
        return abs(a - b)


class OperationFactory:
    _operations = {
        'add': Addition,
        'subtract': Subtraction,
        'multiply': Multiplication,
        'divide': Division,
        'power': Power,
        'root': Root,
        'modulus': Modulus,
        'int_divide': IntegerDivision,
        'percent': Percentage,
        'abs_diff': AbsoluteDifference
    }

    @classmethod
    def create(cls, name: str) -> Operation:
        op_class = cls._operations.get(name.lower())
        if not op_class:
            raise ValidationError(f"Unknown operation '{name}'.")
        return op_class()
