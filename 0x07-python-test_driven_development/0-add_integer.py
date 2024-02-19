#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    - a: an integer or float
    - b: an integer or float (default is 98)

    Returns:
    An integer, the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
