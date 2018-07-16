"""Insert Sorted. 

Given a sorted linked list and a value to insert,
write a function to insert the value in sorted way.

Time Complexity: O(n)
"""
from lib.linkedlist import Node, LinkedList

def insertsorted(head, data):
    node = Node(data)

    if not head:
        return node
    else:
        if head.data > node.data:
            node.next = head
            return node
        else:
            cur = head
            while cur.next:
                if cur.next.data > node.data:
                    next = cur.next
                    cur.next = node
                    node.next = next
                    return head
                else:
                    cur = cur.next
            cur.next = node
            return head

def _get_all_data(head):
    cur = head
    result = []
    while cur:
        result.append(cur.data)
        cur = cur.next
    return result

def test_insert_sorted_one():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)

    head = insertsorted(ll.head, 4)

    assert(_get_all_data(head)==[1,2,3,4,4])


def test_insert_sorted_two():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(5)
    ll.push(10)

    head = insertsorted(ll.head, 3)

    assert(_get_all_data(head)==[1,2,3,5,10])

def test_insert_sorted_three():
    ll = LinkedList()
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(10)

    head = insertsorted(ll.head, 1)

    assert(_get_all_data(head)==[1,3,4,5,10])

def test_insert_sorted_four():
    ll = LinkedList()
    head = insertsorted(ll.head, 10)

    assert(_get_all_data(head)==[10])

def test_insert_sorted_five():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)

    head = insertsorted(ll.head, 10)

    assert(_get_all_data(head)==[1,2,3,4,10])
