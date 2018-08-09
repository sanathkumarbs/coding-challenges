"""MergeSort.

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves,
calls itself for the two halves and then merges the two sorted halves.

The merge() function is used for merging two halves. The merge(arr, l, m, r) is
key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges
the two sorted sub-arrays into one. See following C implementation for details.

MergeSort(arr[], l,  r)

If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

The following diagram from wikipedia shows the complete merge sort process for an
example array {38, 27, 43, 3, 9, 82, 10}. If we take a closer look at the diagram, 
we can see that the array is recursively divided in two halves till the size becomes 1.

Once the size becomes 1, the merge processes comes into action and starts merging
arrays back till the complete array is merged.

https://www.geeksforgeeks.org/merge-sort/
"""
def mergesort(arr, start, end):
    if start >= end:
        return 

    mid = start + (end-start)/2

    mergesort(arr, start, mid)
    mergesort(arr, mid+1, end)

    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    n1 = (mid - start + 1)
    n2 = (end - mid)

    arr1 = [None] * n1
    arr2 = [None] * n2

    for index in range(n1):
        arr1[index] = arr[start + index]

    for index in range(n2):
        arr2[index] = arr[mid + 1 + index]

    i = 0
    j = 0
    curr = start

    while(i < n1 and j < n2):
        if arr1[i] <= arr2[j]:
            arr[curr] = arr1[i]
            curr += 1
            i += 1
        else:
            arr[curr] = arr2[j]
            curr += 1
            j += 1

    while(i < n1):
        arr[curr] = arr1[i]
        curr += 1
        i += 1

    while(j < n2):
        arr[curr] = arr2[j]
        curr += 1
        j += 1


def test_mergesort_one():
    ip = [5, 1, 2, 4, 3, 6]
    op = [1, 2, 3, 4, 5, 6]

    mergesort(ip, 0, len(ip)-1)
    print(ip)
    assert(ip == op)

def test_mergesort_two():
    ip = [9, 3, 83, 9, 2, 0, 1, 65, 2, 822, 9, 11, 22, 3, 3, 3, 47]
    op = [0, 1, 2, 2, 3, 3, 3, 3, 9, 9, 9, 11, 22, 47, 65, 83, 822]

    mergesort(ip, 0, len(ip)-1)
    print(ip)
    assert(ip == op)

def test_mergesort_three():
    ip = [-5, -6, -7, 0, 0, 0, 0, -8, 1, 2, 3]
    op = [-8, -7, -6, -5, 0, 0, 0, 0, 1, 2, 3]

    mergesort(ip, 0, len(ip)-1)
    print(ip)
    assert(ip == op)


