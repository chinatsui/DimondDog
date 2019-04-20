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


class Solution(object):
    @staticmethod
    def remove_nth_from_end(head, n):
        if not head and n:
            return head

        fast = head
        while n:
            fast = fast.next
            n -= 1

        prev, slow = None, head
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        if prev:
            prev.next = slow.next
        else:
            # in the case of delete first node
            head = head.next

        return head
