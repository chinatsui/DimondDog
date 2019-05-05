"""
LeetCode-148

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
from algorithm.core.linked_list import ListNode


class Solution:

    def sort_list(self, head):
        if not head or not head.next:
            return head

        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        l1 = self.sort_list(head)
        l2 = self.sort_list(slow)

        return self.merge(l1, l2)

    @staticmethod
    def merge(l1, l2):
        cur = sentry = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return sentry.next
