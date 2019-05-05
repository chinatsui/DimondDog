"""
LeetCode-147

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs
within the sorted list, and inserts it there.

It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
from algorithm.core.linked_list import ListNode
from algorithm.core.linked_list import ListNodeUtil


class Solution(object):
    @staticmethod
    def insertion_sort_list(head):
        if not head or not head.next:
            return head

        sentry = ListNode(0)
        sentry.next = head
        prev, cur, _next = head, head.next, None

        while cur:
            _next = cur.next
            sm_prev, sm = sentry, sentry.next
            swapped = False
            while sm != cur:
                if sm.val > cur.val:
                    prev.next = cur.next
                    cur.next = sm
                    sm_prev.next = cur
                    swapped = True
                    break
                else:
                    sm_prev = sm
                    sm = sm.next

            if not swapped:
                prev = cur
            cur = _next

        return sentry.next


t_head = ListNodeUtil.build_linked_list([-1, 5, 3, 4, 0])
print(ListNodeUtil.iterate(Solution().insertion_sort_list(t_head)))
