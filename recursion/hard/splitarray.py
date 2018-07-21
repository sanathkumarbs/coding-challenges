"""Split Array. 

Given an array of ints, is it possible to divide
the ints into two groups, so that the sums of the
two groups are the same.

Every int must be in one group or the other.

Write a recursive helper method that takes whatever
arguments you like, and make the initial call to your
recursive helper from splitArray().

No loops needed.

splitarray([2, 2]) == True
splitarray([2, 3]) == False
splitarray([5, 2, 3]) == True

http://codingbat.com/prob/p185204
"""

def splitarray(nums):
    pass

def test_splitarray_one():
    assert(splitarray([2, 2]) == True)

def test_splitarray_two():
    assert(splitarray([2, 3]) == False)

def test_splitarray_three():
    assert(splitarray([5, 2, 3]) == True)