"""String Count. 

Given a string and a non-empty substring sub, compute recursively
the number of times that sub appears in the string, without the
sub strings overlapping.

strCount("catcowcat", "cat") > 2
strCount("catcowcat", "cow") > 1
strCount("catcowcat", "dog") > 0

http://codingbat.com/prob/p186177
"""

def strcount(input, sub, index=0, count=0):
    if index == len(input):
        return count
    else:
        if index >= len(sub) - 1:
            start = index - len(sub) + 1
            end = index + 1

            if input[start:end] == sub:
                count += 1
        
        index += 1
        return strcount(input, sub, index, count)


def test_strcount_one():
    assert(strcount(input="catcowcat", sub="cat") == 2)

def test_strcount_two():
    assert(strcount(input="catcowcat", sub="cow") == 1)

def test_strcount_three():
    assert(strcount(input="catcowcat", sub="dog") == 0)