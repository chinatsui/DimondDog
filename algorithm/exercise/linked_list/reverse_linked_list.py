"""
LeetCode-206

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class Solution(object):
    @staticmethod
    def reverse_list(head):
        if head is None:
            return None

        cur = head
        while cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = head
            head = nxt
        return head
