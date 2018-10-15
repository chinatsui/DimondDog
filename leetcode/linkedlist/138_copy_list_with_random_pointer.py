from leetcode.util.linked_list import RandomListNode


class Solution(object):
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
