"""End X. 

Given a string, compute recursively a new string
where all the lowercase 'x' chars have been moved
to the end of the string.

endX("xxre") > "rexx"
endX("xxhixx") > "hixxxx"
endX("xhixhix") > "hihixxx"

http://codingbat.com/prob/p105722
"""

def endx(input, index=0, ch="", x=""):
    if index == len(input):
        return ch + x
    else:
        if input[index] == "x":
            x += "x"
        else:
            ch += input[index]

        index += 1

        return endx(input, index, ch, x)

def test_endx_one():
    assert(endx("xxre") == "rexx")

def test_endx_two():
    assert(endx("xxhixx") == "hixxxx")

def test_endx_three():
    assert(endx("xhixhix") == "hihixxx")