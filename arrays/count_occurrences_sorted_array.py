""" Count number of occurrences in a sorted array.

Given a sorted array arr[] and a number x, write a function
that counts the occurrences of x in arr[].

Expected time complexity is O(Logn)

Examples:

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
  Output: 4 // x (or 2) occurs 4 times in arr[]

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
  Output: 1 

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
  Output: 2 

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
  Output: -1 // 4 doesn't occur in arr[] 

https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
"""

class Solution(object):
    def count_occurrences(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = self._binarysearch(nums, 0, len(nums)-1, target)
        
        if result == -1:
            return -1
        else:
            start = self._getstart(nums, result, target)
            end = self._getend(nums, result, target)
            return (end - start + 1)
            
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

def test_count_occurrences_one():
    s = Solution()
    assert(s.count_occurrences([1, 1, 2, 2, 2, 2, 3], 2) == 4)

def test_count_occurrences_two():
    s = Solution()
    assert(s.count_occurrences([1, 1, 2, 2, 2, 2, 3], 3) == 1)

def test_count_occurrences_three():
    s = Solution()
    assert(s.count_occurrences([1, 1, 2, 2, 2, 2, 3], 1) == 2)

def test_count_occurrences_four():
    s = Solution()
    assert(s.count_occurrences([1, 1, 2, 2, 2, 2, 3], 4) == -1)