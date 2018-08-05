"""Duplindrome.

Given a word in stack (one letter in each entry), return true if the word is a
"duplindrome" or not.

You do not know the size of the stack.
You can use constant memory.
Do not use any other data structures (other than stacks).

A duplindrome is a palindrome where duplicates are considered as one.

madam => palindrome and duplindrome
mmmmmmmmadam is not a palindrome, but is a duplindrome (as multiple M's are considered as one)
mmaaddam is a duplindrome (not a palindrome)

Note:
Assume all lowercase, and only letters a-z
"""
from stacks.lib.stacks import ArrayStack

def isduplindrome(ip):
    cleaned, length = cleanstack(ip)
    if isstackpalindrome(cleaned, length, ip):
        return True
    return False

def cleanstack(ip):
    length = 0
    cleaned = ArrayStack()

    while not ip.isempty:
        if cleaned.top != ip.top:
            cleaned.push(ip.top)
            ip.pop()
            length += 1
        else:
            ip.pop()
    
    return cleaned, length

def isstackpalindrome(ip, length, temp=None):
    print ip.stack

    if not temp:
        temp = ArrayStack()

    odd = False
    if length % 2 != 0:
        odd = True

    for _ in range(0, int(length/2)):
        temp.push(ip.top)
        ip.pop()

    if odd:
        ip.pop()

    while not ip.isempty:
        if ip.top != temp.top:
            return False

        ip.pop()
        temp.pop()

    return True


def test_isduplindrome_one():
    ip = ArrayStack()
    ip.push('m')
    ip.push('m')
    ip.push('a')
    ip.push('d')
    ip.push('a')
    ip.push('m')

    assert(isduplindrome(ip) == True)


def test_isduplindrome_two():
    ip = ArrayStack()
    ip.push('m')
    ip.push('a')
    ip.push('d')
    ip.push('a')
    ip.push('m')

    assert(isduplindrome(ip) == True)


def test_isduplindrome_three():
    ip = ArrayStack()
    ip.push('m')
    ip.push('a')
    ip.push('d')
    ip.push('m')

    assert(isduplindrome(ip) == False)

def test_isduplindrome_four():
    ip = ArrayStack()
    ip.push('m')
    ip.push('m')
    ip.push('m')
    ip.push('m')

    assert(isduplindrome(ip) == True)