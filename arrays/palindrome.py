"""Palindrome.

Given a word, check if it is a palindrome or not.
"""

def palindrome_iterative(word):
    """Iterative implementation of finding if a word is palindrome."""
    for i in range(0, len(word)//2):
        if word[i].lower() != word[len(word)-i-1].lower():
            return False
    return True

def test_palindrome_iterative_one():
    """Test Palindrome Iterative Implementation."""
    word = "mom"
    assert(palindrome_iterative(word)==True)

def test_palindrome_iterative_two():
    """Test Palindrome Iterative Implementation."""
    word = "mat"
    assert(palindrome_iterative(word)==False)

def test_palindrome_iterative_three():
    """Test Palindrome Iterative Implementation."""
    word = "noon"
    assert(palindrome_iterative(word)==True)

def test_palindrome_iterative_four():
    """Test Palindrome Iterative Implementation."""
    word = "nOon"
    assert(palindrome_iterative(word)==True)

def test_palindrome_iterative_five():
    """Test Palindrome Iterative Implementation."""
    word = "a"
    assert(palindrome_iterative(word)==True)

def test_palindrome_iterative_six():
    """Test Palindrome Iterative Implementation."""
    word = "test"
    assert(palindrome_iterative(word)==False)
