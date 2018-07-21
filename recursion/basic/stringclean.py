"""String Clean. 

Given a string, return recursively a "cleaned" string
where adjacent chars that are the same have been
reduced to a single char.

So "yyzzza" yields "yza".

stringclean("yyzzza") == "yza"
stringclean("abbbcdd") == "abcd"
stringclean("Hello") == "Helo"

http://codingbat.com/prob/p104029
"""

def stringclean(input):
    if len(input) < 2:
        return input
    
    if input[0] == input[1]:
        return stringclean(input[1:])

    return input[0] + stringclean(input[1:])

def test_stringclean_one():
    assert(stringclean("yyzzza") == "yza")

def test_stringclean_two():
    assert(stringclean("abbbcdd") == "abcd")

def test_stringclean_three():
    assert(stringclean("Hello") == "Helo")