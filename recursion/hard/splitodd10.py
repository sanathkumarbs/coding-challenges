"""Split Odd 10. 

Given an array of ints, is it possible to divide the ints
into two groups, so that the sum of one group is a multiple
of 10, and the sum of the other group is odd.

Every int must be in one group or the other.

Write a recursive helper method that takes whatever arguments
you like, and make the initial call to your recursive helper
from splitOdd10(). 

No loops needed.

splitodd10([5, 5, 5]) == True
splitodd10([5, 5, 6]) == False
splitodd10([5, 5, 6, 1]) == True

http://codingbat.com/prob/p171660
"""

def splitodd10(nums):
    pass

def test_splitodd10_one():
    assert(splitodd10([5, 5, 5]) == True)

def test_splitodd10_two():
    assert(splitodd10([5, 5, 6]) == False)

def test_splitodd10_three():
    assert(splitodd10([5, 5, 6, 1]) == True)

