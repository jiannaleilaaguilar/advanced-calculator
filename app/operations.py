from abc import ABC, abstractmethod
from app.exceptions import OperationError, ValidationError

class Operation(ABC):
    """Abstract Base Class for all calculator operations."""
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

# --- Basic Operations ---
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

# --- Mandatory Advanced Operations ---
class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b

class Root(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Zeroth root is undefined.")
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of a negative number is undefined in real numbers.")
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
            raise OperationError("Division by zero in percentage calculation.")
        return (a / b) * 100.0

class AbsoluteDifference(Operation):
    def execute(self, a: float, b: float) -> float:
        return abs(a - b)

# --- Factory Pattern ---
class OperationFactory:
    """Factory class to create Operation instances based on command names."""
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
        'abs_diff': AbsoluteDifference,
    }

    @classmethod
    def create(cls, op_name: str) -> Operation:
        op_class = cls._operations.get(op_name.lower())
        if not op_class:
            raise ValidationError(f"Unknown operation '{op_name}'.")
        return op_class()
