"""
This module contains unit tests for the functions in the example module.
"""

from example import add, subtract


def test_add():
    """
    Test the add function.
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """
    Test the subtract function.
    """
    assert subtract(5, 3) == 2
    assert subtract(10, -5) == 15
    assert subtract(0, 0) == 0
