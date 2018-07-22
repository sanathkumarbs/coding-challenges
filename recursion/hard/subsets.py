"""Subsets. 

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

https://leetcode.com/problems/subsets/description/
"""
from copy import deepcopy

def subsets(nums):
    # subset = [None] * len(nums)
    result = []
    subset = []
    gensubsets(nums, subset, 0, result)
    print result

# def gensubsets(nums, subset, index):
#     if index >= len(nums):
#         print subset
#         return

#     # considering NOT to add the current index
#     subset[index] = None
#     gensubsets(nums, subset, index+1)

#     # considering to add the current index
#     subset[index] = nums[index]
#     gensubsets(nums, subset, index+1)

def gensubsets(nums, subset, index, results):
    if index >= len(nums):
        # print subset
        results.append(subset)
        return

    # considering NOT to add the current index
    outsubset = deepcopy(subset)
    gensubsets(nums, outsubset, index+1, results)

    # considering to add the current index
    insubset = deepcopy(subset)
    if insubset:
        insubset.append(nums[index])
    else:
        insubset = [nums[index]]
    gensubsets(nums, insubset, index+1, results)

def test_subsets_one():
    subsets([1,2,3])