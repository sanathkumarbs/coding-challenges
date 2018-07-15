"""Pair Star. 

Given a string, compute recursively a new string where
identical chars that are adjacent in the original
string are separated from each other by a "*".

pairStar("hello") > "hel*lo"
pairStar("xxyy") > "x*xy*y"
pairStar("aaaa") > "a*a*a*a"

http://codingbat.com/prob/p158175
"""

def pairstar(input, index=0, output=None):
    if index == len(input):
        return output
    else:
        if output:
            if output[-1] == input[index]:
                output += "*"
            
            output += input[index]
        else:
            output = input[index]
        
        index += 1
        return pairstar(input, index, output)

def test_pairstar_one():
    assert(pairstar("hello") == "hel*lo")

def test_pairstar_two():
    assert(pairstar("xxyy") == "x*xy*y")

def test_pairstar_three():
    assert(pairstar("aaaa") == "a*a*a*a")