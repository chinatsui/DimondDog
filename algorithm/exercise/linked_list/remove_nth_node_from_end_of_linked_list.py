"""
LeetCode-19

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
from algorithm.core.linked_list import ListNode


class Solution(object):
    @staticmethod
    def remove_nth_from_end(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        slow = ListNode(0)
        slow.next = head
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        if slow.next == head:
            return head.next
        else:
            slow.next = slow.next.next

        return head
