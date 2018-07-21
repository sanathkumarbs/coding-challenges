"""Count X. 

Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

countX("xxhixx") > 4
countX("xhixhix") > 3
countX("hi") > 0

http://codingbat.com/prob/p170371
"""

def countx(data, count=0):
    if not data:
        return count
    else:
        if data[-1] == "x":
            count += 1
        data = data[:-1]
        return countx(data, count)


def test_countx_one():
    assert(countx("xxhixx") == 4)

def test_countx_two():
    assert(countx("xhixhix") == 3)

def test_countx_three():
    assert(countx("hi") == 0)