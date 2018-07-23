"""Split 53. 

Given an array of ints, is it possible to divide
the ints into two groups, so that the sum of the
two groups is the same, with these constraints:

1. All the values that are multiple of 5 must be in one group
2. All the values that are a multiple of 3 (and not a multiple of 5)
   must be in the other.
   
No loops needed.

split53([1, 1]) == True
split53([1, 1, 1]) == False
split53([2, 4, 2]) == True

http://codingbat.com/prob/p168295
"""
def split53(nums, index=0, mult5=0, mult3=0):
    if index >= len(nums):
        if mult3 == mult5:
            return True
        return False

    if nums[index] % 5 == 0 and nums[index] % 3 == 0:
        return split53(nums, index+1, mult5 + nums[index], mult3)
    elif nums[index] % 3 == 0:
        return split53(nums, index+1, mult5, mult3 + nums[index])
    else:
        if split53(nums, index+1, mult5 + nums[index], mult3):
            return True
        else:
            return split53(nums, index+1, mult5, mult3 + nums[index])

def test_split53_one():
    assert(split53([1, 1]) == True)

def test_split53_two():
    assert(split53([1, 1, 1]) == False)

def test_split53_three():
    assert(split53([2, 4, 2]) == True)