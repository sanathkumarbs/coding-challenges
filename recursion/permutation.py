"""Permutations. """

def permute(input, output=""):
    if len(input) == 0:
        print output
    else:
        for index in range(len(input)):
            noutput = output + input[index]
            ninput = input[:index] + input[index+1:]
            permute(ninput, noutput)

def test_permute_one():
    permute(input="ABCD")