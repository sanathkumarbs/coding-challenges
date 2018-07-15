"""Count ABC. 

Count recursively the total number of "abc" and "aba"
substrings that appear in the given string.

countAbc("abc") > 1
countAbc("abcxxabc") > 2
countAbc("abaxxaba") > 2

http://codingbat.com/prob/p161124
"""

def countabc(input, index=0, count=0):
    if index >= len(input):
        return count
    else:
        if index >= 2:
            if input[index-2:index+1] == "abc" or input[index-2:index+1] == "aba":
                count += 1
        index += 1
        return countabc(input, index, count)

def test_countabc_one():
    assert(countabc("abc") == 1)

def test_countabc_two():
    assert(countabc("abcxxabc") == 2)

def test_countabc_three():
    assert(countabc("abaxxaba") == 2)