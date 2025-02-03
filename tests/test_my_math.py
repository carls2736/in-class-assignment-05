import pytest
import src.my_math as my_math
def multiply(a, b):
    return a * b

def difference(a, b):
    return a - b

def absolute_sum(a, b):
    return abs(a) + abs(b)


def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():
    res = multiply(2, 3)
    assert res == 6


# Check for understanding
## Test difference
def test_difference():
    res = difference(5, 2)
    assert res == 3

# Work together
## Test absolute sum
def test_absolute_sum():
    res = absolute_sum(2, -3)
    assert res == 5

def test_it_should_return_positive_numbers_2():
    res = absolute_sum(-1, 2)
    assert res == 3

# Check for understanding
## Test calculate age
def calculate_age():
    res = calculate_age(2021, 25, True)
    assert res == 1996
   

