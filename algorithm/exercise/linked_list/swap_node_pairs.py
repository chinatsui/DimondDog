"""
LeetCode-24

Given a linked list, swap every two adjacent nodes and return its head.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

Note:
    Your algorithm should use only constant extra space.
    You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
from algorithm.core.linked_list import ListNode


class Solution:
    @staticmethod
    def swap_pairs(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        first = head
        second = head.next
        while first and second:
            second_next = second.next
            first.next = second_next
            second.next = first
            prev.next = second
            prev = first
            first = first.next
            if first:
                second = first.next

        return dummy.next
