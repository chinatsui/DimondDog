"""
LeetCode-141

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


class Solution(object):
    @staticmethod
    def has_cycle(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None or head.next.next is None:
            return False

        slow = head.next
        fast = head.next.next

        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
