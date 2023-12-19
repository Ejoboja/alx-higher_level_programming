#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides a by b and prints the result.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division or None if division by zero or a type error occurs.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
