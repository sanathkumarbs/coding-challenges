"""Split List Odd Even.

Given a singly linked list with integer data, create two lists,
one with all odd elements, and one with even.
"""
from lib.linkedlist import LinkedList

def splitoddeven(head):
    oddhead = head
    evenhead = None

    oddcur = oddhead
    evencur = evenhead

    oddprev = None

    while oddcur:
        if (oddcur.data % 2) == 0:
            if evencur:
                evencur.next = oddcur
                evencur = evencur.next
            else:
                evenhead = oddcur
                evencur = evenhead

            next = evencur.next
            evencur.next = None
            oddcur = next

            if oddprev:
                oddprev.next = next
            else:
                oddhead = next

        else:
            oddprev = oddcur
            oddcur = oddcur.next
    
    return oddhead, evenhead

def _get_all_data(head):
    cur = head
    result = []
    while cur:
        result.append(cur.data)
        cur = cur.next
    return result

def isoddlist(head):
    cur = head
    while cur:
        if (cur.data % 2) == 0:
            return False
        cur = cur.next
    return True

def isevenlist(head):
    cur = head
    while cur:
        if (cur.data % 2) != 0:
            return False
        cur = cur.next
    return True

def test_splitoddeven_one():
    ll = LinkedList()
    ll.push(1)
    ll.push(3)
    ll.push(4)
    ll.push(2)
    ll.push(9)

    print(_get_all_data(ll.head))

    odd, even = splitoddeven(ll.head)

    print(_get_all_data(odd))
    print(_get_all_data(even))

    assert(isoddlist(odd) == True)
    assert(isevenlist(even) == True)

def test_splitoddeven_two():
    ll = LinkedList()
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(2)
    ll.push(9)

    print(_get_all_data(ll.head))

    odd, even = splitoddeven(ll.head)

    print(_get_all_data(odd))
    print(_get_all_data(even))

    assert(isoddlist(odd) == True)
    assert(isevenlist(even) == True)


def test_splitoddeven_three():
    ll = LinkedList()
    ll.push(2)
    ll.push(4)
    ll.push(6)
    ll.push(8)
    ll.push(10)

    print(_get_all_data(ll.head))

    odd, even = splitoddeven(ll.head)

    print(_get_all_data(odd))
    print(_get_all_data(even))

    assert(isoddlist(odd) == True)
    assert(isevenlist(even) == True)

def test_splitoddeven_four():
    ll = LinkedList()
    ll.push(1)
    ll.push(3)
    ll.push(9)
    ll.push(5)
    ll.push(7)

    print(_get_all_data(ll.head))

    odd, even = splitoddeven(ll.head)

    print(_get_all_data(odd))
    print(_get_all_data(even))

    assert(isoddlist(odd) == True)
    assert(isevenlist(even) == True)

def test_splitoddeven_five():
    ll = LinkedList()
    ll.push(2)
    ll.push(6)
    ll.push(4)
    ll.push(2)
    ll.push(9)

    print(_get_all_data(ll.head))

    odd, even = splitoddeven(ll.head)

    print(_get_all_data(odd))
    print(_get_all_data(even))

    assert(isoddlist(odd) == True)
    assert(isevenlist(even) == True)

def test_splitoddeven_six():
    ll = LinkedList()

    print(_get_all_data(ll.head))

    odd, even = splitoddeven(ll.head)

    print(_get_all_data(odd))
    print(_get_all_data(even))

    assert(isoddlist(odd) == True)
    assert(isevenlist(even) == True)