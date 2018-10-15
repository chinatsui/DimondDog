from leetcode.util.linked_list import ListNode


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
