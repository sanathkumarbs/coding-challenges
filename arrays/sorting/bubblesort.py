"""Bubble Sort.

The bubble sort makes multiple passes through a list. It compares adjacent items
and exchanges those that are out of order. Each pass through the list places the
next largest value in its proper place. In essence, each item “bubbles” up to
the location where it belongs.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubblesort(arr):
    """Bubble Sort a given array."""
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

    return arr

def test_bubble_sort_one():
    """Test Bubble Sort."""
    arr = [5,1,4,2,8,9]
    assert(bubblesort(arr)==[1,2,4,5,8,9])