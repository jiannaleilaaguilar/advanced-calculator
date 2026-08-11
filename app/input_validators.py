from app.exceptions import ValidationError


def validate_number(value_str: str, max_val: float) -> float:
    try:
        val = float(value_str)
    except ValueError:
        raise ValidationError(
            f"Invalid input '{value_str}'. Input must be a valid number."
        )

    if abs(val) > max_val:
        raise ValidationError(
            f"Input {val} exceeds maximum allowable limit of {max_val}."
        )
    return val
