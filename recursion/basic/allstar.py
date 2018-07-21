"""All Star. 

Given a string, compute recursively a new string where
all the adjacent chars are now separated by a "*".

allStar("hello") > "h*e*l*l*o"
allStar("abc") > "a*b*c"
allStar("ab") > "a*b"

http://codingbat.com/prob/p183394
"""

def allstar(input, index=0):
    if index == len(input) - 1:
        return input[index]

    return input[index] + "*" + allstar(input, index=index+1)

def test_allstar_one():
    assert(allstar("hello") == "h*e*l*l*o")

def test_allstar_two():
    assert(allstar("abc") == "a*b*c")

def test_allstar_three():
    assert(allstar("ab") == "a*b")
