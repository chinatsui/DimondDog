from leetcode.util.linked_list import ListNode


class Solution:
    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        cur = dummy_node
        sum = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum += l1_val + l2_val
            cur_digit = sum % 10
            sum //= 10
            cur.next = ListNode(cur_digit)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if sum > 0:
            cur.next = ListNode(sum)

        return dummy_node.next
