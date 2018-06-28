#!/usr/bin/env python
"""Reverse a LinkedList.

Given pointer to the head node of a linked list, the task is to reverse the
linked list. We need to reverse the list by changing links between nodes.
"""

from lib.linkedlist import LinkedList


def reverse_iterative(head):
    """Reverse a linkedlist iteratively and return its head."""
    cur = head
    prev = None

    while cur is not None:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next

    head = prev

    return head


class TestIterative(object):
    """Test class to test reverse_iterative."""

    def _get_sample_linkedlist(self, size=4):
        """Create a sample linkedlist and return the linkedlist obj."""
        ll = LinkedList()

        for item in range(size):
            ll.push(item)

        return ll

    def test_one(self):
        """Testing reverse of a linkedlist."""
        ll = self._get_sample_linkedlist()
        ll.head = reverse_iterative(ll.head)

        assert(ll.get(0).data == 3)
        assert(ll.get(1).data == 2)
        assert(ll.get(2).data == 1)
        assert(ll.get(3).data == 0)

    def test_two(self):
        """Testing reverse of a linkedlist of size one."""
        ll = self._get_sample_linkedlist(size=1)
        ll.head = reverse_iterative(ll.head)

        assert(ll.get(0).data == 0)

    def test_three(self):
        """Testing reverse of an empty linkedlist."""
        ll = LinkedList()
        ll.head = reverse_iterative(ll.head)

        assert(ll.head is None)
