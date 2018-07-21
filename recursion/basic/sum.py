"""Sum of n numbers. 

Calculate num of n numbers recursively.
"""

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

def test_sum_one():
    assert(sum(1)==1)

def test_sum_two():
    assert(sum(2)==3)

def test_sum_three():
    assert(sum(5)==15)