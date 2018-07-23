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

def groupsum5(index, nums, target):
    if target == 0:
        return True
    
    if index >= len(nums):
        return False

    if nums[index] % 5 == 0:
        return groupsum5(index+1, nums, target-nums[index])
    else:
        if index > 0:
            if nums[index-1] % 5 == 0 and nums[index] == 1:
                return groupsum5(index+1, nums, target)
        
        if groupsum5(index+1, nums, target-nums[index]):
            return True
        else:
            return groupsum5(index+1, nums, target)

def test_groupsum5_one():
    assert(groupsum5(0, [2, 5, 10, 4], 19) == True)

def test_groupsum5_two():
    assert(groupsum5(0, [2, 5, 10, 4], 17) == True)

def test_groupsum5_three():
    assert(groupsum5(0, [2, 5, 10, 4], 12) == False)