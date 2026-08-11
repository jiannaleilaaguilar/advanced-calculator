from app.exceptions import ValidationError

def validate_number(val, max_val=None) -> float:
    """Validates and converts a string input into a float."""
    try:
        num = float(val)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid input '{val}'. Input must be a valid number.")
    
    if max_val is not None and abs(num) > max_val:
        raise ValidationError(f"Input value {num} exceeds maximum allowed boundary ({max_val}).")
    
    return num
