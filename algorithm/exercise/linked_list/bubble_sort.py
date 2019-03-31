"""
Input: 2->1->3->10->7->4
Output: 1->2->3->4->7->10
"""
from algorithm.core.linked_list import ListNodeUtil


class Solution:

    @staticmethod
    def sort(head):
        if not head:
            return

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        for i in range(n):
            cur = head
            for j in range(n - i - 1):
                nxt = cur.next
                if cur.val > nxt.val:
                    cur.val, nxt.val = nxt.val, cur.val
                cur = cur.next

        return head


t_node = ListNodeUtil.build_linked_list([2, 1, 3, 10, 7, 4])
t_node = Solution().sort(t_node)
print(ListNodeUtil.iterate(t_node))
