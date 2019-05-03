"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from algorithm.core.binary_tree import TreeNode


class Solution:
    def sorted_list_to_bst(self, head):
        if not head:
            return

        prev, slow, fast = None, head, head.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        cur = TreeNode(slow.val)

        # left child
        if prev:
            prev.next = None
            cur.left = self.sorted_list_to_bst(head)

        # right child
        if slow.next:
            cur.right = self.sorted_list_to_bst(slow.next)

        return cur
