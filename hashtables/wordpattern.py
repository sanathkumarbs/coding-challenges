"""Word Pattern. 

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

https://leetcode.com/problems/word-pattern/description/
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern:
            return False
        
        if not str:
            return False
        
        words = str.split()
        
        if len(pattern) != len(words):
            return False
        
        mapping = {}
        reversemap = {}
        
        for index in range(len(pattern)):
            if pattern[index] not in mapping:
                if words[index] not in reversemap:
                    mapping[pattern[index]] = words[index]
                    reversemap[words[index]] = True
                else:
                    return False
            else:
                if mapping[pattern[index]] != words[index]:
                    return False
                
        return True