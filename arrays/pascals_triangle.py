#!/usr/bin/env python
"""Pascals Triangle."""

# Pascals Triangle - 1

# Given a non-negative integer numRows,
# generate the first numRows of Pascal's triangle.

# https://leetcode.com/problems/pascals-triangle/description/

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

import math

def pascals_triangle_1(limit=5):
    result = []
    for i in range(limit):
        row = []
        for j in range(i):
            val = 1
            if j != 0 and j != i:
                val = result[i-1][j] + result[i-1][j-1]
            row.append(val)
        result.append(row)
    return result

def test_pascals_triangle_1_one():
    print(pascals_triangle_1(limit=5))

# Pascals Triangle - 2

# Given a non-negative index k where k ≤ 33, 
# return the kth index row of the Pascal's triangle.

# https://leetcode.com/problems/pascals-triangle-ii/description/

# Input: 3
# Output: [1,3,3,1]