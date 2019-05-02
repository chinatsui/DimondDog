"""
LeetCode-94

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:

    def inorder_traversal(self, root):
        res, stack = [], []
        self._push_nodes(stack, root)

        while stack:
            node = stack.pop()
            res.append(node.val)
            self._push_nodes(stack, node.right)
        return res

    @staticmethod
    def _push_nodes(stack, node):
        while node:
            stack.append(node)
            node = node.left


t_root = bt.deserialize([1, None, 2, 3])
print(Solution().inorder_traversal(t_root))
