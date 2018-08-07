"""QuickSort.

QuickSort is a Divide and Conquer algorithm. It picks an element as
pivot and partitions the given array around the picked pivot.

There are many different versions of quickSort that pick pivot in different ways.

> Always pick first element as pivot.
> Always pick last element as pivot (implemented below)
> Pick a random element as pivot.
> Pick median as pivot.

The key process in quickSort is partition().
Target of partitions is, given an array and an element x of array as pivot,
put x at its correct position in sorted array and put all smaller elements
(smaller than x) before x, and put all greater elements (greater than x) after x.
All this should be done in linear time.
"""
import random

def quicksort(arr, start, end):
    if start >= end:
        return 

    pivot = choosepivot(arr, start, end)
    newpivot = partition(arr, start, end, pivot)

    quicksort(arr, start, newpivot - 1)
    quicksort(arr, newpivot + 1, end)

def choosepivot(arr, start, end):
    return random.randint(start, end)

def partition(arr, start, end, pivot):
    arr[pivot], arr[end] = arr[end], arr[pivot]

    newpivot = start

    for curr in range(start, end):
        if arr[curr] <= arr[end]:
            arr[newpivot], arr[curr] = arr[curr], arr[newpivot]
            newpivot += 1

    arr[newpivot], arr[end] = arr[end], arr[newpivot]

    return newpivot


def test_quicksort_one():
    ip = [5, 1, 2, 4, 3, 6]
    op = [1, 2, 3, 4, 5, 6]

    quicksort(ip, 0, len(ip)-1)
    print(ip)
    assert(ip == op)

def test_quicksort_two():
    ip = [9, 3, 83, 9, 2, 0, 1, 65, 2, 822, 9, 11, 22, 3, 3, 3, 47]
    op = [0, 1, 2, 2, 3, 3, 3, 3, 9, 9, 9, 11, 22, 47, 65, 83, 822]

    quicksort(ip, 0, len(ip)-1)
    print(ip)
    assert(ip == op)

def test_quicksort_three():
    ip = [-5, -6, -7, 0, 0, 0, 0, -8, 1, 2, 3]
    op = [-8, -7, -6, -5, 0, 0, 0, 0, 1, 2, 3]

    quicksort(ip, 0, len(ip)-1)
    print(ip)
    assert(ip == op)