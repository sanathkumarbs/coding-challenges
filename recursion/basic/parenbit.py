"""ParenBit. 

Given a string that contains a single pair of parenthesis,
compute recursively a new string made of only of the parenthesis
and their contents, so "xyz(abc)123" yields "(abc)".

parenBit("xyz(abc)123") > "(abc)"
parenBit("x(hello)") > "(hello)"
parenBit("(xy)1") > "(xy)"

http://codingbat.com/prob/p137918
"""
def parenbit(input, output= "", index=0, paren=False):
    if index == len(input):
        return output
    else:
        if input[index] == "(" and not paren:
            paren = True

        if paren:
            output += input[index]

        if input[index] == ")" and paren:
            paren = False

        index += 1
        return parenbit(input, output, index, paren)

def test_parenbit_one():
    assert(parenbit("xyz(abc)123") == "(abc)")

def test_parenbit_two():
    assert(parenbit("x(hello)") == "(hello)")

def test_parenbit_thee():
    assert(parenbit("(xy)1") == "(xy)")

def test_parenbit_four():
    assert(parenbit("abc") == "")