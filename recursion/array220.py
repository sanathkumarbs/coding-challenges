"""Array 220. 

Given an array of ints, compute recursively if the array
contains somewhere a value followed in the array by that
value times 10.

We'll use the convention of considering only the part of
the array that begins at the given index. In this way, a
recursive call can pass index+1 to move down the array.

The initial call will pass in index as 0.

array220([1, 2, 20], 0) > true
array220([3, 30], 0) > true
array220([3], 0) > false

http://codingbat.com/prob/p173469
"""

def array220(input, index=0):
    if index == len(input) - 1:
        return False
    else:
        if input[index] * 10 == input[index + 1]:
            return True
        
        index += 1
        return array220(input, index)

def test_array220_one():
    assert(array220([1, 2, 20]) == True)

def test_array220_two():
    assert(array220([3, 30]) == True)

def test_array220_three():
    assert(array220([3]) == False)