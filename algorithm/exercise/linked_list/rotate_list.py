"""
LeetCode-61

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
from algorithm.core.linked_list import ListNode
from algorithm.core.linked_list import ListNodeUtil


class Solution(object):

    @staticmethod
    def rotate_right(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head

        i, cur, tail = 0, head, dummy
        while cur:
            tail = cur
            cur = cur.next
            i += 1

        j = i - k % i

        if j == i:
            return head

        prv = dummy
        cur = head
        while j > 0:
            prv = cur
            cur = cur.next
            j -= 1

        dummy.next = cur
        tail.next = head
        prv.next = None

        return dummy.next


t_node = ListNodeUtil.build_linked_list([1, 2])
res = Solution().rotate_right(t_node, 2)
print(ListNodeUtil.iterate(res))
