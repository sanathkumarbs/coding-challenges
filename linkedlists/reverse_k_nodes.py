"""Reverse Nodes in k-Group.

NOTE: TODO

Given a linked list, reverse the nodes of a linkedlist k at a time
and return its modified list.

k is a positive integer and is less than or equal to the length of
the linked list. If the number of nodes is not a multiple of k then
left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

1. Only constant extra memory is allowed.
2. You may not alter the values in the
list's nodes, only nodes itself may be changed.

https://leetcode.com/problems/reverse-nodes-in-k-group
"""
from lib.linkedlist import LinkedList

def reverse(head, k):
    pass
    # length = 0

    # cur = head
    # while cur is not None:
    #     length += 1
    #     cur = cur.next

    # splits = int(length/k)

    # cur = head
    # prev = None
    # for _ in range(splits):
    #     n = 3
    #     while n != 0:
    #         next = cur.next
    #         cur.next = prev

    #         prev = cur
    #         cur = next

    #         n -= 1

def reverse_knodes(head, k):
    cur = head
    while cur is not None:
        knode = _get_kth_node(cur, k)
        if knode:
            pass

def _get_kth_node(head, k):
    for _ in range(k):
        if head is not None:
            head = head.next
        else:
            return None

    return head

