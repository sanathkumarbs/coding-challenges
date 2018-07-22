"""Group Sum. 

Given an array of ints, is it possible to choose a
group of some of the ints, such that the group sums
to the given target?

This is a classic backtracking recursion problem.

Once you understand the recursive backtracking
strategy in this problem, you can use the same
pattern for many problems to search a space of choices.

Rather than looking at the whole array, our convention
is to consider the part of the array starting at index
start and continuing to the end of the array.

The caller can specify the whole array simply by passing
start as 0.

No loops are needed. 
The recursive calls progress down the array.

groupsum(0, [2, 4, 8], 10) == True
groupsum(0, [2, 4, 8], 14) == True
groupsum(0, [2, 4, 8], 9) == False

http://codingbat.com/prob/p145416
"""

def groupsum(index, nums, target):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    if groupsum(index+1, nums, target):
        return True
    else:
        return groupsum(index+1, nums, target - nums[index])

    
def test_groupsum_one():
    assert(groupsum(0, [2, 4, 8], 10) == True)

def test_groupsum_two():
    assert(groupsum(0, [2, 4, 8], 14) == True)

def test_groupsum_three():
    assert(groupsum(0, [2, 4, 8], 9) == False)