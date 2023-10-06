import pytest
from ex import *


def test_sum_int_valid():
    assert sum_int(2, 3) == 5
    assert sum_int(-1, 1) == 0


def test_sum_int_invalid():
    with pytest.raises(TypeError):
        sum_int("2", 3)
    with pytest.raises(TypeError):
        sum_int(2, "3")


def test_quadratic_equation_real_solutions():
    assert quadratic_equation(1.0, -3.0, 2.0) == (2.0, 1.0)


def test_quadratic_equation_no_real_solutions():
    assert quadratic_equation(1.0, 1.0, 1.0) is None


def test_check_palindrome_true():
    assert check_palindrome("racecar") is True
    assert check_palindrome("level") is True


def test_check_palindrome_false():
    assert check_palindrome("python") is False


def test_sum_age_valid():
    assert sum_age(2023) == 202278


def test_sum_age_invalid():
    with pytest.raises(TypeError):
        sum_age("1990")


def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(8) == 21
    assert fibonacci(10) == 55
