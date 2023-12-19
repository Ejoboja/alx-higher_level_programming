#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Executes a function safely and handles exceptions.

    Args:
        fct (function): The function to execute.
        *args: Variable number of arguments to pass to the function.

    Returns:
        The result of the function. Returns None if an exception occurs.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
