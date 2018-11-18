"""
LeetCode-142

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


class Solution(object):
    @staticmethod
    def detect_cycle(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return None

        slow = head.next
        fast = head.next.next
        while slow and fast and fast.next:
            if slow == fast:
                cycle_begin = head
                while cycle_begin != slow:
                    cycle_begin = cycle_begin.next
                    slow = slow.next
                return cycle_begin
            slow = slow.next
            fast = fast.next.next
        return None
