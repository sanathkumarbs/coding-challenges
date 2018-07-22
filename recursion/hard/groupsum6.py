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

def groupsum6(index, nums, target):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    if nums[index] == 6:
        return groupsum6(index+1, nums, target-nums[index])
    else:
        if groupsum6(index+1, nums, target):
            return True
        else:
            return groupsum6(index+1, nums, target-nums[index])

def test_groupsum6_one():
    assert(groupsum6(0, [5, 6, 2], 8) == True)

def test_groupsum6_two():
    assert(groupsum6(0, [5, 6, 2], 9) == False)

def test_groupsum6_three():
    assert(groupsum6(0, [5, 6, 2], 7) == False)
