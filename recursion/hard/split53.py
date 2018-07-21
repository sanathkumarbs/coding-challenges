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
def split53(nums):
    pass

def test_split53_one():
    assert(split53([1, 1]) == True)

def test_split53_two():
    assert(split53([1, 1, 1]) == False)

def test_split53_three():
    assert(split53([2, 4, 2]) == True)