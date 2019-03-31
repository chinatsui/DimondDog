"""
LeetCode-234

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
from algorithm.core.linked_list import ListNode


class Solution(object):
    def is_palindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        slow = head.next
        fast = head.next.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = self._reserve(slow)

        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True

    @staticmethod
    def _reserve(head):
        if head:
            cur = head
            while cur.next:
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = head
                head = nxt
        return head


t_head = ListNode(0)
t_head.next = ListNode(0)
print(Solution().is_palindrome(t_head))
