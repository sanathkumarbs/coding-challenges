"""Group Sum 5. 

Given an array of ints, is it possible to choose a
group of some of the ints, such that the group sums
to the given target with these additional constraints:

1. All multiples of 5 in the array must be included in the group.
2. If the value immediately following a multiple of 5 is 1, it must not be chosen.

No loops needed.

groupsum5(0, [2, 5, 10, 4], 19) == True
groupsum5(0, [2, 5, 10, 4], 17) == True
groupsum5(0, [2, 5, 10, 4], 12) == False

http://codingbat.com/prob/p138907
"""

def groupsum5(start, nums, target):
    pass

def test_groupsum5_one():
    assert(groupsum5(0, [2, 5, 10, 4], 19) == True)

def test_groupsum5_two():
    assert(groupsum5(0, [2, 5, 10, 4], 17) == True)

def test_groupsum5_three():
    assert(groupsum5(0, [2, 5, 10, 4], 12) == False)