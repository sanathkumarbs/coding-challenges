"""No X. 

Given a string, compute recursively a new string
where all the 'x' chars have been removed.

noX("xaxb") > "ab"
noX("abc") > "abc"
noX("xx") > ""

http://codingbat.com/prob/p118230
"""

def nox(input, index=0, output=""):
    if index == len(input):
        return output
    else:
        if input[index] != "x":
            output += input[index]
        index += 1
        return nox(input, index, output)

def test_nox_one():
    assert(nox("xaxb") == "ab")

def test_nox_two():
    assert(nox("abc") == "abc")

def test_nox_three():
    assert(nox("xx") == "")