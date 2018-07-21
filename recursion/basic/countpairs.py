"""Count Pairs. 

We'll say that a "pair" in a string is two instances
of a char separated by a char.

So "AxA" the A's make a pair.

Pair's can overlap, so "AxAxA" contains 3 pairs
-- 2 for A and 1 for x.

Recursively compute the number of pairs in the given string.

countpairs("axa") == 1
countpairs("axax") == 2
countpairs("axbx") == 1

http://codingbat.com/prob/p154048
"""

def countpairs(input):
    if len(input) < 3:
        return 0

    if input[0] == input[2]:
        return 1 + countpairs(input[1:])

    return countpairs(input[1:])

def test_countpairs_one():
    assert(countpairs("axa") == 1)

def test_countpairs_two():
    assert(countpairs("axax") == 2)

def test_countpairs_three():
    assert(countpairs("axbx") == 1)