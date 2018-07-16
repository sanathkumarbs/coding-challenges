"""Merge Sorted Lists. 

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

https://leetcode.com/problems/merge-two-sorted-lists/description/
"""
from lib.linkedlist import LinkedList

class Solution(object):
    def mergeTwoLists(self, head1, head2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        prev = None
        
        if not head1:
            return head2
        
        if not head2:
            return head1
        
        if not head1 and head2:
            return head
        
        if head1.data <= head2.data:
            head = head1
            head1cur = head1
            head2cur = head2
        else:
            head = head2
            head1cur = head2
            head2cur = head1

        # import pdb
        # pdb.set_trace()
            
        while head1cur and head2cur:
            if head1cur.data <= head2cur.data:
                prev = head1cur
                head1cur = head1cur.next
            else:
                next = head1cur
                prev.next = head2cur
                head2cur = head2cur.next
                prev.next.next = next
                prev = prev.next
        
        if head1cur:
            prev.next = head1cur
        
        if head2cur:
            prev.next = head2cur
                
        return head

def _get_all_data(head):
    cur = head
    result = []
    while cur:
        result.append(cur.data)
        cur = cur.next
    return result

def test_mergetwolists_one():
    ll1 = LinkedList()
    ll1.push(-10)
    ll1.push(-10)
    ll1.push(-9)
    ll1.push(-4)
    ll1.push(1)
    ll1.push(6)
    ll1.push(6)

    ll2 = LinkedList()
    ll2.push(-7)

    solution = Solution()
    head = solution.mergeTwoLists(ll1.head, ll2.head)

    result = _get_all_data(head)
    assert(result==[-10,-10,-9,-7,-4,1,6,6])



