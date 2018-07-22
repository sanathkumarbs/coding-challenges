"""Group No Adjacent. 

Given an array of ints, is it possible to choose a
group of some of the ints, such that the group sums
to the given target with this additional constraint:

If a value in the array is chosen to be in the group, 
the value immediately following it in the array must
not be chosen.

No loops needed.

groupnoadj(0, [2, 5, 10, 4], 12) == True
groupnoadj(0, [2, 5, 10, 4], 14) == False
groupnoadj(0, [2, 5, 10, 4], 7) == False

http://codingbat.com/prob/p169605
"""

def groupnoadj(index, nums, target):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    # NOT choosing the current number
    if groupnoadj(index+1, nums, target):
        return True
    else:
        # choosing the current number
        return groupnoadj(index+2, nums, target-nums[index])

def test_groupnoadj_one():
    assert(groupnoadj(0, [2, 5, 10, 4], 12) == True)

def test_groupnoadj_two():
    assert(groupnoadj(0, [2, 5, 10, 4], 14) == False)

def test_groupnoadj_three():
    assert(groupnoadj(0, [2, 5, 10, 4], 7) == False)