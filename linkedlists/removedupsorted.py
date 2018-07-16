"""Remove Duplicates from Sorted List.

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""

from lib.linkedlist import LinkedList

def deleteduplicates(head):
    cur = head
        
    while cur and cur.next:
        if cur.next.data == cur.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

def _get_all_data(head):
    cur = head
    result = []
    while cur:
        result.append(cur.data)
        cur = cur.next
    return result

def test_deleteduplicates_one():
    ll = LinkedList()
    ll.push(1)
    ll.push(1)
    ll.push(1)

    head = deleteduplicates(ll.head)
    result = _get_all_data(head)

    assert(result == [1])

def test_deleteduplicates_two():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)

    head = deleteduplicates(ll.head)
    result = _get_all_data(head)

    assert(result == [1, 2, 3])

def test_deleteduplicates_three():
    ll = LinkedList()
    ll.push(1)
    ll.push(1)
    ll.push(2)
    ll.push(2)
    ll.push(2)
    ll.push(2)
    ll.push(2)
    ll.push(5)
    ll.push(5)
    ll.push(5)

    head = deleteduplicates(ll.head)
    result = _get_all_data(head)

    assert(result == [1, 2, 5])


