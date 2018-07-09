"""Word Pyramid.

NOTE: TODO
 
Given an input string, write a program to print it in multiple lines such that
each line should be longer than the previous line by at least one letter.
 
Goal is to maximize the number of lines in output.
"""
 
def word_pyramid(sentence):
    """Compute the Word Pyramid for a given sentence.
 
    Time complexity: O(n)
    Space complexity: O(n)

    Assumptions:
    1. No punctuations are in the text, just words (lowercase letters) and single spaces.
    2. Length of word overflow < intmax
    2. The output is just prints and not an array
    3. Allowed to use extra space?
    4. Duplicate words are considered two different words
    5. Sentence is a valid string and not None
    6. Cannot reuse words which have been printed in a line already

    Questions:
    1. Greedy fails for test_word_pyramid_two. Come up with a DP solution?
    """
    index = 0
    prev = 0
    remaining = len(sentence)
 
    buf = ""
    while index < len(sentence):
        if sentence[index] != " ":
            buf += sentence[index]
            index += 1
            remaining -= 1
        else:
            if len(buf) > prev and (remaining - 1) > len(buf):
                print buf
                index += 1
                remaining -= 1
                prev = len(buf)
                buf = ""
            elif len(buf) > prev and (remaining - 1) <= len(buf):
                buf = buf + sentence[index:]
                index = len(sentence)
                print buf
                buf = ""
            else:
                buf += sentence[index]
                index += 1
                remaining -= 1
 
    if buf:
        print buf
 
def test_word_pyramid():
    sentence = "a twist in the tale is a good that i read last week"
    print "\n --- NEW TEST --- \n"
    print "Input: {0} \n ".format(sentence)
    word_pyramid(sentence)
 
def test_word_pyramid_one():
    sentence = "a twist in the tale is a good that i read last"
    print "\n --- NEW TEST --- \n"
    print "Input: {0} \n ".format(sentence)
    word_pyramid(sentence)

def test_word_pyramid_two():
    sentence = "clever joe lumberjacks will cut now"
    print "\n --- NEW TEST --- \n"
    print "Input: {0} \n ".format(sentence)
    word_pyramid(sentence)

def test_word_pyramid_three():
    sentence = ""
    print "\n --- NEW TEST --- \n"
    print "Input: {0} \n ".format(sentence)
    word_pyramid(sentence)
 
if __name__ == "__main__":
    test_word_pyramid()
    test_word_pyramid_one()
    test_word_pyramid_two()