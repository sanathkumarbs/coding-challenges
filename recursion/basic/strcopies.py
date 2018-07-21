"""Str Copies. 

Given a string and a non-empty substring sub, compute recursively
if at least n copies of sub appear in the string somewhere,
possibly with overlapping. N will be non-negative.

strCopies("catcowcat", "cat", 2) > true
strCopies("catcowcat", "cow", 2) > false
strCopies("catcowcat", "cow", 1) > true

http://codingbat.com/prob/p118182
"""

def strcopies(input, sub, n, start=0, count=0):
    end = start + len(sub)

    if count >= n:
        return True

    if end > len(input) + 1:
        if count >= n:
            return True
        return False
    else:
        if input[start:end] == sub:
            count += 1

        return strcopies(input, sub, n, start=start+1, count=count)

def test_strcopies_one():
    assert(strcopies("catcowcat", "cat", 2) == True)

def test_strcopies_two():
    assert(strcopies("catcowcat", "cow", 2) == False)

def test_strcopies_three():
    assert(strcopies("catcowcat", "cow", 1) == True)

