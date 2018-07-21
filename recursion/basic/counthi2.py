"""Count Hi 2. 

Given a string, compute recursively the number of times
lowercase "hi" appears in the string, however do not
count "hi" that have an 'x' immedately before them.

counthi2("ahixhi") == 1
counthi2("ahibhi") == 2
counthi2("xhixhi") == 0

http://codingbat.com/prob/p143900
"""

def counthi2(input):
    if len(input) < 3:
        if input == "hi":
            return 1
        return 0

    if input[0] == "x" and input[1:3] == "hi":
        return counthi2(input[3:])
    elif input[0:2] == "hi":
        return 1 + counthi2(input[2:])
    return counthi2(input[1:])

def test_counthi2_one():
    assert(counthi2("ahixhi") == 1)

def test_counthi2_two():
    assert(counthi2("ahibhi") == 2)

def test_counthi2_three():
    assert(counthi2("xhixhi") == 0)