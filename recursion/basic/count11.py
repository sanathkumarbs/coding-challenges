"""Count 11. 


Given a string, compute recursively (no loops) the
number of "11" substrings in the string.

The "11" substrings should not overlap.

count11("11abc11") > 2
count11("abc11x11x11") > 3
count11("111") > 1

http://codingbat.com/prob/p167015
"""

def count11(input, count=0, index=0, prev=False):
    if index == len(input):
        return count
    else:
        if index >= 1:
            if input[index-1:index+1] == "11":
                if not prev:
                    count += 1
                    prev = True
                else:
                    prev = False
            else:
                prev = False
        index += 1
        return count11(input, count, index, prev)

def test_count11_one():
    assert(count11("11abc11") == 2)

def test_count11_two():
    assert(count11("abc11x11x11") == 3)

def test_count11_three():
    assert(count11("111") == 1)

def test_count11_four():
    assert(count11("1111abc111") == 3)