"""
LeetCode-145

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:
    def postorder_traversal(self, root):
        res, stack = [], []
        self._push_nodes(stack, root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if stack and node == stack[-1].left:
                self._push_nodes(stack, stack[-1].right)
        return res

    @staticmethod
    def _push_nodes(stack, node):
        while node:
            stack.append(node)
            node = node.left if node.left else node.right


t_root = bt.deserialize([1, None, 2, 3])
print(Solution().postorder_traversal(t_root))
