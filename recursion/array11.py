"""Array 11. 

Given an array of ints, compute recursively the number of times that
the value 11 appears in the array. We'll use the convention of
considering only the part of the array that begins at the given index.

In this way, a recursive call can pass index+1 to move down the array.
The initial call will pass in index as 0.

array11([1, 2, 11], 0) > 1
array11([11, 11], 0) > 2
array11([1, 2, 3, 4], 0) > 0

http://codingbat.com/prob/p135988
"""

def array11(input, index=0, count=0):
    if index >= len(input):
        return count
    else:
        if input[index] == 11:
            count += 1

        index += 1
        return array11(input, index, count)

def test_array11_one():
    assert(array11(input=[1, 2, 11], index=0) == 1)

def test_array11_two():
    assert(array11(input=[11, 11], index=0) == 2)

def test_array11_three():
    assert(array11(input=[1, 2, 3, 4], index=0) == 0)
