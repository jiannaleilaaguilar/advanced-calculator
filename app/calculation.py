from datetime import datetime

class Calculation:
    """Represents a single calculation record."""
    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Serializes the calculation into a dictionary format."""
        return {
            'operation': self.operation,
            'a': self.a,
            'b': self.b,
            'result': self.result,
            'timestamp': self.timestamp
        }
