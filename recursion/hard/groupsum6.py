"""Group Sum 6. 

Given an array of ints, is it possible to choose a
group of some of the ints, beginning at the start
index, such that the group sums to the given target?

However, with the additional constraint that all
6's must be chosen.

No loops needed.

groupsum6(0, [5, 6, 2], 8) == True
groupsum6(0, [5, 6, 2], 9) == False
groupsum6(0, [5, 6, 2], 7) == False

http://codingbat.com/prob/p199368
"""

def groupsum6(start, nums, target):
    pass

def test_groupsum6_one():
    assert(groupsum6(0, [5, 6, 2], 8) == True)

def test_groupsum6_two():
    assert(groupsum6(0, [5, 6, 2], 9) == False)

def test_groupsum6_three():
    assert(groupsum6(0, [5, 6, 2], 7) == False)
