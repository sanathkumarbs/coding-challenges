"""Valid Palindrome. 

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

https://leetcode.com/problems/valid-palindrome/description/
"""
import re

def ispalindrome(s):
    if len(s) <= 1: 
        return True
    return s[0] == s[-1] and ispalindrome(s[1:-1])

def cleanup(s):
    s = s.lower()
    s = re.sub('[^0-9a-zA-Z]+', '', s)
    return s

def test_ispalindrome_one():
    """Test Palindrome Recursive Implementation."""
    word = "mom"
    assert(ispalindrome(word)==True)

def test_ispalindrome_two():
    """Test Palindrome Recursive Implementation."""
    word = "mat"
    assert(ispalindrome(word)==False)

def test_ispalindrome_three():
    """Test Palindrome Recursive Implementation."""
    word = "noon"
    assert(ispalindrome(word)==True)

def test_ispalindrome_four():
    """Test Palindrome Recursive Implementation."""
    word = "nOon"
    word = cleanup(word)
    assert(ispalindrome(word)==True)

def test_ispalindrome_five():
    """Test Palindrome Recursive Implementation."""
    word = "a"
    assert(ispalindrome(word)==True)

def test_ispalindrome_six():
    """Test Palindrome Recursive Implementation."""
    word = "test"
    assert(ispalindrome(word)==False)

def test_ispalindrome_seven():
    """Test Palindrome Recursive Implementation."""
    word = "A man, a plan, a canal: Panama"
    word = cleanup(word)
    assert(ispalindrome(word)==True)

def test_ispalindrome_eight():
    """Test Palindrome Recursive Implementation."""
    word = "race a car"
    word = cleanup(word)
    assert(ispalindrome(word)==False)