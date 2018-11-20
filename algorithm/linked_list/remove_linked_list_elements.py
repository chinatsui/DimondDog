"""
LeetCode-203

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
from algorithm.util.linked_list import ListNode


class Solution(object):
    @staticmethod
    def remove_elements(head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head

        prev = dummy_head
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next

        return dummy_head.next
