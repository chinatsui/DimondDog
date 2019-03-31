"""
LeetCode-138

A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""
from algorithm.core.linked_list import RandomListNode


class Solution1(object):
    @staticmethod
    def copy_random_list(head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cache = {}
        dummy_node = RandomListNode(0)
        cur = dummy_node
        while head:
            if head in cache:
                new_node = cache[head]
            else:
                new_node = RandomListNode(head.label)

            if head.random:
                new_random_node = RandomListNode(head.random.label)
                new_node.random = new_random_node
                cache[head.random] = new_random_node

            cur.next = new_node
            cur = cur.next
            head = head.next
        return dummy_node.next


class Solution2:
    """
        o-->o-->o-->o-->o
    =>  o-->x-->o-->x-->o-->x-->o-->x-->o-->x
    =>  do random link
    =>  restore to x-->x-->x-->x-->x
    """
    @staticmethod
    def copy_random_list(head):
        cur = head
        while cur:  # Deduplicate each node and link it to the original node one by one
            copy = RandomListNode(cur.label)
            nxt = cur.next
            cur.next = copy
            copy.next = nxt
            cur = nxt

        cur = head
        while cur:  # Link random pointer for each deduplicate node.
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        pseudoHead = RandomListNode(0)
        pseudoCur = pseudoHead
        while cur:  # Restore the answer.
            copy = cur.next
            pseudoCur.next = copy
            pseudoCur = pseudoCur.next
            cur.next = copy.next
            cur = cur.next

        return pseudoHead.next
