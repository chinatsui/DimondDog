from leetcode.util.linked_list import ListNode


class Solution(object):
    def rotate_right(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0:
            return head

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        k %= length

        if k == 0:
            return head

        left = self.reserve(head)
        right = left

        right_prev = None
        for i in range(k):
            right_prev = right
            right = right.next
        right_prev.next = None

        left = self.reserve(left)
        right = self.reserve(right)

        right_prev = left
        while right_prev.next:
            right_prev = right_prev.next
        right_prev.next = right

        return left

    @staticmethod
    def reserve(head):
        if head:
            cur = head
            while cur.next:
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = head
                head = nxt
        return head
