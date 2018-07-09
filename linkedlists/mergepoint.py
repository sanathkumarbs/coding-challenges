"""Intersection of Two Linked Lists.

NOTE: TODO

Write a program to find the node at which the intersection of
two singly linked lists begins.

https://leetcode.com/problems/intersection-of-two-linked-lists

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:
1. If the two linked lists have no intersection at all, return null.
2. The linked lists must retain their original structure after the function returns.
3. You may assume there are no cycles anywhere in the entire linked structure.
4. Your code should preferably run in O(n) time and use only O(1) memory.
"""
from lib.linkedlist import LinkedList

def mergenode_extraspace(head1, head2):
    indexed = {}
    cur = head1

    while cur is not None:
        indexed[cur] = cur.data
        cur = cur.next

    cur = head2
    while cur is not None:
        if cur in indexed:
            return cur
        cur = cur.next

def mergenode_noextraspace(head1, head2):
    return True

def test_merge_node():
    ll = LinkedList()
    ll.push(3)
    ll.push(1)
    ll.push(2)

    ll_one = LinkedList()
    ll_one.push(10)
    ll_one.push(20)

    ll_two = LinkedList()
    ll_two.push(5)

    ll_one.get(1).next = ll.head
    ll_two.get(0).next = ll.head

    assert(mergenode_extraspace(ll_one.head, ll_two.head).data == 3)

def test_merge_node_noextraspace():
    ll = LinkedList()
    ll.push(3)
    ll.push(1)
    ll.push(2)

    ll_one = LinkedList()
    ll_one.push(10)
    ll_one.push(20)

    ll_two = LinkedList()
    ll_two.push(5)

    ll_one.get(1).next = ll.head
    ll_two.get(0).next = ll.head

    # assert(mergenode_noextraspace(ll_one.head, ll_two.head).data == 3)


