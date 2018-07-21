"""Count 8. 

Given a non-negative int n, compute recursively (no loops)
the count of the occurrences of 8 as a digit, except that
an 8 with another 8 immediately to its left counts double,
so 8818 yields 4.

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

count8(8) > 1
count8(818) > 2
count8(8818) > 4

http://codingbat.com/prob/p192383
"""

def count8(num, count=0):
    if num == 0:
        return count
    else:
        if num % 10 == 8:
            count += 1

        if num % 100 == 88:
            count += 1

        num = num/10

        return count8(num, count)

def test_count8_one():
    assert(count8(8) == 1)

def test_count8_two():
    assert(count8(818) == 2)

def test_count8_three():
    assert(count8(8818) == 4)

def test_count8_four():
    assert(count8(8288818) == 7)