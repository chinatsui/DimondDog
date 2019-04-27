"""
LeetCode-82

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
"""
from algorithm.core.linked_list import ListNode


class Solution:
    @staticmethod
    def delete_duplicates(head):
        if not head:
            return head

        sentry = ListNode(0)
        sentry.next = head

        prev, cur = sentry, head
        while head.next:
            head = head.next
            if cur.val != head.val:
                cur.next = head
                prev = cur
                cur = cur.next
            else:
                prev.next = None
                while head.next:
                    head = head.next
                    if cur.val != head.val:
                        cur = head
                        prev.next = cur
                        break

        return sentry.next
