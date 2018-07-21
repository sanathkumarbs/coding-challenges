"""Nest Paren. 

Given a string, return true if it is a nesting of zero
or more pairs of parenthesis, like "(())" or "((()))". 

Suggestion: check the first and last chars,
and then recur on what's inside them.

nestparen("(())") == True
nestparen("((()))") == True
nestparen("(((x))") == False

http://codingbat.com/prob/p183174
"""
def nestparen(input):
    if len(input) == 0:
        return True

    if len(input) == 1:
        return False

    if input[0] == "(" and input[-1] == ")":
        return nestparen(input[1:-1])

    return False

def test_nestparen_one():
    assert(nestparen("(())") == True)

def test_nestparen_two():
    assert(nestparen("((()))") == True)

def test_nestparen_three():
    assert(nestparen("(((x))") == False)