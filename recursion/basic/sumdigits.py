"""Sum Digits. 

Given a non-negative int n, return the sum of its digits
recursively (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

sumDigits(126) > 9
sumDigits(49) > 13
sumDigits(12) > 3

http://codingbat.com/prob/p163932
"""

def sumdigits(num, sum=0):
    if num == 0:
        return sum
    else:
        sum += num % 10

        return sumdigits(num/10, sum=sum)

def test_sumdigits_one():
    assert(sumdigits(126)==9)

def test_sumdigits_two():
    assert(sumdigits(49)==13)

def test_sumdigits_three():
    assert(sumdigits(12)==3)