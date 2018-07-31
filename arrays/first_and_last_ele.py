"""Find First and Last Position of Element in Sorted Array.

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = self._binarysearch(nums, 0, len(nums)-1, target)
        
        if result == -1:
            return [-1, -1]
        else:
            start = self._getstart(nums, result, target)
            end = self._getend(nums, result, target)
            return [start, end]
            
    def _getstart(self, nums, index, target):
        while index - 1 >= 0 and nums[index - 1] == target:
            index -= 1
        return index
    
    def _getend(self, nums, index, target):
        while index + 1 < len(nums) and nums[index + 1] == target:
            index += 1
        return index
        
    def _binarysearch(self, nums, low, high, target):
        if low > high:
            return -1
        
        mid = low + ((high - low) / 2)
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] > target:
                return self._binarysearch(nums, low, mid-1, target)
            else:
                return self._binarysearch(nums, mid+1, high, target)

def test_searchrange_one():
    s = Solution()
    assert(s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])

def test_searchrange_two():
    s = Solution()
    assert(s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])