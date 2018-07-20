"""Array 6. 

Given an array of ints, compute recursively if the array 
contains a 6.

We'll use the convention of considering only the part of
the array that begins at the given index.

In this way, a recursive call can pass index+1 to move down
the array.

The initial call will pass in index as 0.

array6([1, 6, 4], 0) > True
array6([1, 4], 0) > False
array6([6], 0) > True

http://codingbat.com/prob/p108997
"""

def array6(input, index=0):
    if index >= len(input):
        return False

    if input[index] == 6:
        return True

    return array6(input, index=index+1)

def test_array6_one():
    assert(array6([1, 6, 4], 0)==True)

def test_array6_two():
    assert(array6([1, 4], 0)==False)

def test_array6_three():
    assert(array6([6], 0)==True)