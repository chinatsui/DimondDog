"""
LeetCode-430

You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure,
as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""
from algorithm.core.linked_list import Node


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
