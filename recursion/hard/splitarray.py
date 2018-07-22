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

Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.

Note:
1. Each of the array element will not exceed 100.
2. The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

https://leetcode.com/problems/partition-equal-subset-sum/description/
"""

def canPartition(arr):
    total = sum(arr)

    if total % 2 != 0:
        return False

    if len(set(list(arr))) == 1:
        if len(arr) % 2 == 0:
            return True
        else:
            return False

    return splitarray(arr, index=0, group1sum=0, group2sum=0)

def splitarray(arr, index=0, group1sum=0, group2sum=0):
    if index >= len(arr):
        if group1sum == group2sum and group1sum != 0:
            return True
        return False

    if splitarray(arr, index + 1, group1sum + arr[index], group2sum):
        return True
    else:
        return splitarray(arr, index + 1, group1sum, group2sum + arr[index])


def test_splitarray_one():
    assert(splitarray([2, 2]) == True)

def test_splitarray_two():
    assert(splitarray([2, 3]) == False)

def test_splitarray_three():
    assert(splitarray([5, 2, 3]) == True)

def test_splitarray_four():
    assert(splitarray([1, 2, 3, 5]) == False)

def test_splitarray_five():
    assert(splitarray([1, 5, 11, 5]) == True)