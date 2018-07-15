"""Count 7. 

Given a non-negative int n, return the count of the occurrences of 7 as a digit.

So for example 717 yields 2. (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


count7(717) > 2
count7(7)   > 1
count7(123) > 0

http://codingbat.com/prob/p101409
"""

def count7(num, count=0):
    if num < 9:
        if num % 10 == 7:
            count += 1
        return count
    else:
        if num % 10 == 7:
            count += 1
        return count7(int(num/10), count)
    
def test_count7_one():
    assert(count7(717) == 2)

def test_count7_two():
    assert(count7(7) == 1)

def test_count7_three():
    assert(count7(123) == 0)