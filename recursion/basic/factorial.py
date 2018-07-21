"""Factorial of n.

Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1.
Compute the result recursively (without loops).

factorial(1) > 1
factorial(2) > 2
factorial(3) > 6

http://codingbat.com/prob/p154669
"""

def factorial(n):
    # base case
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def test_factorial_one():
    assert(factorial(1) == 1)

def test_factorial_two():
    assert(factorial(2) == 2)

def test_factorial_three():
    assert(factorial(3) == 6)