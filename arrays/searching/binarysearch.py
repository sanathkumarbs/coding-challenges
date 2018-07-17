"""Binary Search.

Given a sorted (in ascending order) integer array nums of n elements
and a target value, write a function to search target in nums.

If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

1. You may assume that all elements in nums are unique.
2. n will be in the range [1, 10000].
3. The value of each element in nums will be in the range [-9999, 9999].
"""

def binarysearch(arr, start, end, item):
    if start > end:
        return -1
    
    mid = int(start + (end-start)/2)

    if item == arr[mid]:
        return mid
    else:
        if item < arr[mid]:
            return binarysearch(arr, start, mid-1, item)
        else:
            return binarysearch(arr, mid+1, end, item)

def test_binarysearch_one():
    arr = [1,2,3,4,5,6,7,8,9]
    item = 2
    assert(binarysearch(arr, 0, len(arr)-1, item)==1)

def test_binarysearch_two():
    arr = [1,2,3,4,5,6,7,8,9]
    item = 10
    assert(binarysearch(arr, 0, len(arr)-1, item)==-1)