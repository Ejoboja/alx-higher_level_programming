#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a NameError exception with a specified message.

    Args:
        message (str): Custom message for the exception.

    Raises:
        NameError: Always raises a NameError with the provided message.
    """
    raise NameError(message)
