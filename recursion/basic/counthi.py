"""Count Hi. 

Given a string, compute recursively (no loops)
the number of times lowercase "hi" appears in the string.

countHi("xxhixx") > 1
countHi("xhixhix") > 2
countHi("hi") > 1

http://codingbat.com/prob/p184029
"""

def counthi(input, index=0, count=0):
    if index == len(input):
        return count 
    else:
        if input[index-1:index+1] == "hi":
            count += 1

        index += 1
        return counthi(input, index, count)

def test_counthi_one():
    assert(counthi("xxhixx") == 1)

def test_counthi_two():
    assert(counthi("xhixhix") == 2)

def test_counthi_three():
    assert(counthi("hi") == 1)