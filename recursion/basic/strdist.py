"""String Distance. 

Given a string and a non-empty substring sub,
compute recursively the largest substring which
starts and ends with sub and return its length.

strdist("catcowcat", "cat") == 9
strdist("catcowcat", "cow") == 3
strdist("cccatcowcatxx", "cat") == 9

http://codingbat.com/prob/p195413
"""
def strdist(input, sub):
    if len(input) < len(sub):
        return 0

    if input[:len(sub)] == sub and input[-len(sub):] == sub:
        return len(input)

    return strdist(input[1:-1], sub)

def test_strdist_one():
    assert(strdist("catcowcat", "cat") == 9)

def test_strdist_two():
    assert(strdist("catcowcat", "cow") == 3)

def test_strdist_three():
    assert(strdist("cccatcowcatxx", "cat") == 9)

