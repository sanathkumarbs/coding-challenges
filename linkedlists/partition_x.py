"""Partition List.

NOTE: TODO

Given a linked list and a value x, partition it such that all
nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes
in each of the two partitions.

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

https://leetcode.com/problems/partition-list
"""
from lib.linkedlist import LinkedList

def partition_x(head, x):
    cur = head
    prev = None
    insertbefore = head

    while cur is not None:
        if cur.data < x:
            next = cur.next
            cur.next = insertbefore

            insertbefore = cur
            prev.next = next

    cur = insertbefore
    prev = head
    while cur is not head:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next

    return head
    

def test_partition_x():
    ll = LinkedList()
    ll.push(1)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(5)
    ll.push(2)

    head = partition_x(ll.head, 3)
    cur = head
    while cur is not None:
        print cur.data
        cur = cur.next


            