from leetcode.util.linked_list import ListNode


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
