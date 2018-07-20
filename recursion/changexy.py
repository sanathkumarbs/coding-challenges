"""Change X Y. 

Given a string, compute recursively (no loops)
a new string where all the lowercase 'x' chars
have been changed to 'y' chars.

changeXY("codex") > "codey"
changeXY("xxhixx") > "yyhiyy"
changeXY("xhixhix") > "yhiyhiy"

http://codingbat.com/prob/p101372
"""

def changexy(input, output="", index=0):
    if index >= len(input):
        return output

    if input[index] == "x":
        output += "y"
    else:
        output += input[index]

    return changexy(input, output=output, index=index+1)

def test_changexy_one():
    assert(changexy("codex") == "codey")

def test_changexy_two():
    assert(changexy("xxhixx") == "yyhiyy")

def test_changexy_three():
    assert(changexy("xhixhix") == "yhiyhiy")