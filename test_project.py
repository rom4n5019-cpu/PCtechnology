import math
import pytest

from project import my_factorial, my_start_str


def test_factorial():
    assert my_factorial(5) == math.factorial(5)
    assert my_factorial(0) == 1


def test_factorial_negative():
    with pytest.raises(ValueError):
        my_factorial(-1)


def test_start_str():
    assert my_start_str() == "Hello world!"
