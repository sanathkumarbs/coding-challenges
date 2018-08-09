"""Selection Sort.

The selection sort improves on the bubble sort by making only one exchange
for every pass through the list.
"""
def selectionsort(arr):
    """Selection Sort a given array."""
    for i in range(len(arr)):
        minindex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        temp = arr[minindex]
        arr[minindex] = arr[i]
        arr[i] = temp
    return arr

def test_bubble_sort_one():
    """Test Selection Sort."""
    arr = [5,1,4,2,8,9]
    assert(selectionsort(arr)==[1,2,4,5,8,9])