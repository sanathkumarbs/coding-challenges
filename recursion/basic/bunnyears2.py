"""Bunny Ears 2. 

We have bunnies standing in a line, numbered 1, 2, ...

The odd bunnies (1, 3, ..) have the normal 2 ears.
The even bunnies (2, 4, ..) we'll say have 3 ears, 
because they each have a raised foot.

Recursively return the number of "ears" in the
bunny line 1, 2, ... n (without loops or multiplication).

bunnyears2(0) == 0
bunnyears2(1) == 2
bunnyears2(2) == 5

http://codingbat.com/prob/p107330
"""

def bunnyears2(n):
    if n == 0:
        return 0

    if (n%2) == 0:
        return 3 + bunnyears2(n-1)

    return 2 + bunnyears2(n-1)

def test_bunnyears2_one():
    assert(bunnyears2(0) == 0)

def test_bunnyears2_two():
    assert(bunnyears2(1) == 2)

def test_bunnyears2_three():
    assert(bunnyears2(2) == 5)