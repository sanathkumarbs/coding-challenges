"""Power of N. 

Given base and n that are both 1 or more, compute
recursively (no loops) the value of base to the
n power, so powerN(3, 2) is 9 (3 squared).

powerN(3, 1) > 3
powerN(3, 2) > 9
powerN(3, 3) > 27

http://codingbat.com/prob/p158888
"""

def powern(base, n):
    if n == 0:
        return 1

    return base * powern(base, n-1)

def test_powern_one():
    assert(powern(3, 1)==3)

def test_powern_two():
    assert(powern(3, 2)==9)

def test_powern_three():
    assert(powern(3, 3)==27)