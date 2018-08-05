"""Reoganize linkedlist such that n, n+1, .. nodes are swapped.

Given a linked list, reorganize it in the following way.
a. Head node 0 remains where it is
b. Node 1-2 are swapped to be 2>1 (0 points to 2)
c. Nodes 3-4-5 are reversed to 5-4-3 (and 1 points to 5)
d. Nodes 6-7-8-9 are reversed to 9-8-7-6 ( and 3 points to 9).
e. And so on...

If there are insufficient nodes just swap however many or left
So 0>1>2>3>4>5>6>7>8>9>10>11 will beccome
0>2>1>5>4>3>9>8>7>6>11>10
"""
from lib.linkedlist import Node, LinkedList

def reorg(head):
    cur = head
    split = 0
    prev = head

    while (cur != None):
        split += 1
        count = 0
        lcur = cur
        start = lcur

        while(lcur != None and count != split):
            count += 1
            end = lcur
            lcur = lcur.next

        next = lcur

        multiswap(prev, next, start, end)

        cur = next
        prev = start

    return head

def multiswap(prev, next, start, end):
    p = start
    cur = start.next

    while(cur != next):
        n = cur.next
        cur.next = p
        p = cur
        cur = n

    prev.next = end
    start.next = next

def _get_all_data(head):
    cur = head
    result = []
    while cur:
        result.append(cur.data)
        cur = cur.next
    return result

def test_reorg_one():
    ll = LinkedList()
    ll.push(0)
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    ll.push(8)
    ll.push(9)
    ll.push(10)
    ll.push(11)

    print " "

    result = _get_all_data(ll.head)
    print result

    head = reorg(ll.head)
    result = _get_all_data(head)
    print result
    
    assert(result == [0,2,1,5,4,3,9,8,7,6,11,10])


def test_reorg_two():
    ll = LinkedList()
    ll.push(0)
    ll.push(1)
    ll.push(2)
    ll.push(3)

    print " "

    result = _get_all_data(ll.head)
    print result

    head = reorg(ll.head)
    result = _get_all_data(head)
    print result
    
    assert(result == [0,2,1,3])