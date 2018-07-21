"""Bunny Ears.

We have a number of bunnies and each bunny has two big floppy ears.
We want to compute the total number of ears across all the bunnies
recursively (without loops or multiplication).

bunnyEars(0) > 0
bunnyEars(1) > 2
bunnyEars(2) > 4

http://codingbat.com/prob/p183649
"""

def bunny_ears(n):
    # base case
    if n == 0:
        return 0
    else:
        return 2 + bunny_ears(n-1)

def test_bunny_ears_one():
    assert(bunny_ears(0) == 0)

def test_bunny_ears_two():
    assert(bunny_ears(1) == 2)

def test_bunny_ears_three():
    assert(bunny_ears(2) == 4)

def test_bunny_ears_four():
    assert(bunny_ears(10) == 20)