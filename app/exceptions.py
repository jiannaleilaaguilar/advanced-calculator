class CalculatorError(Exception):
    """Base exception class for all calculator errors."""
    pass

class OperationError(CalculatorError):
    """Raised when an arithmetic operation fails (e.g., division by zero, undefined roots)."""
    pass

class ValidationError(CalculatorError):
    """Raised when user input fails validation or when an operation is unrecognized."""
    pass
