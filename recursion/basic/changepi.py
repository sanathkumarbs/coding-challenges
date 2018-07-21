"""Change Pi. 

Given a string, compute recursively (no loops) a new string
where all appearances of "pi" have been replaced by "3.14".

changePi("xpix") > "x3.14x"
changePi("pipi") > "3.143.14"
changePi("pip") > "3.14p"

http://codingbat.com/prob/p170924
"""

def changepi(input, output=None):
    if not input:
        return output
    else:
        if output:
            output += input[0]

            if output[-2:] == "pi":
                prefix = output[:-2]
                output = prefix + "3.14"
        else:
            output = input[0]

        return changepi(input[1:], output)

def test_changepi_one():
    assert(changepi("xpix") == "x3.14x")

def test_changepi_two():
    assert(changepi("pipi") == "3.143.14")

def test_changepi_three():
    assert(changepi("pip") == "3.14p")