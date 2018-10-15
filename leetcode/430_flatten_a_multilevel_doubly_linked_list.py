from leetcode.util.linked_list import Node


class Solution(object):
    """
    input: 1---2---3---4---5---6--NULL
                   |
                   7---8---9---10--NULL
                       |
                       11--12--NULL

    output: 1-2-3-7-8-11-12-9-10-4-5-6-NULL
    """
    @staticmethod
    def flatten(head):
        """
        :type head: Node
        :rtype: Node
        """
        prev = None
        cur = head
        stack = [cur]
        while stack:
            cur = stack.pop()
            if prev:
                prev.next = cur
                if cur:
                    cur.prev = prev
            while cur:
                if cur.child:
                    stack.append(cur.next)
                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None
                prev = cur
                cur = cur.next
        return head
