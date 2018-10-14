class Solution(object):
    @staticmethod
    def detect_cycle(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return None

        slow = head.next
        fast = head.next.next
        while slow and fast and fast.next:
            if slow == fast:
                cycle_begin = head
                while cycle_begin != slow:
                    cycle_begin = cycle_begin.next
                    slow = slow.next
                return cycle_begin
            slow = slow.next
            fast = fast.next.next
        return None
