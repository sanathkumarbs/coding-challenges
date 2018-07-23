"""Group Sum Clump. 

Given an array of ints, is it possible to choose
a group of some of the ints, such that the group
sums to the given target.

With this additional constraint:
if there are numbers in the array that are adjacent
and the identical value, they must either all be chosen,
or none of them chosen.

For example, with the array {1, 2, 2, 2, 5, 2},
either all three 2's in the middle must be chosen
or not, all as a group.

one loop can be used to find the extent of the identical values.

groupsumclump(0, [2, 4, 8], 10) == True
groupsumclump(0, [1, 2, 4, 8, 1], 14) == True
groupsumclump(0, [2, 4, 4, 8], 14) == False

http://codingbat.com/prob/p105136
"""

def groupsumclump(index, nums, target):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    if index + 1 < len(nums):
        if nums[index] == nums[index+1]:

            # finding the end of adjacent identical values
            end = index
            while end < len(nums) and nums[end] == nums[index]:
                end += 1

            # not choosing the identical values
            if groupsumclump(end, nums, target):
                return True
            else:
                # choosing the identical values
                newtarget = target - ((end-index) * nums[index])
                return groupsumclump(end, nums, newtarget)
        else:
            if groupsumclump(index+1, nums, target-nums[index]):
                return True
            else:
                return groupsumclump(index+1, nums, target)
    else:
        if groupsumclump(index+1, nums, target-nums[index]):
            return True
        else:
            return groupsumclump(index+1, nums, target)
            

def test_groupsumclump_one():
    assert(groupsumclump(0, [2, 4, 8], 10) == True)

def test_groupsumclump_two():
    assert(groupsumclump(0, [1, 2, 4, 8, 1], 14) == True)

def test_groupsumclump_three():
    assert(groupsumclump(0, [2, 4, 4, 8], 14) == False)

def test_groupsumclump_four():
    assert(groupsumclump(0, [1, 2, 4, 2, 2, 2, 2], 9) == True)

def test_groupsumclump_five():
    assert(groupsumclump(0, [1, 2, 4, 2, 2, 2, 2], 8) == True)

def test_groupsumclump_six():
    assert(groupsumclump(0, [2, 2, 4, 2, 2, 2, 2], 12) == True)
