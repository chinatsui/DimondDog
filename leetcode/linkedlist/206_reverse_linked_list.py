class Solution(object):
    @staticmethod
    def reverse_list(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        cur = head
        while cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = head
            head = nxt
        return head
