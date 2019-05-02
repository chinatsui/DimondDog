"""
LeetCode-144

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:
    @staticmethod
    def preorder_traversal(root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return res


t_root = bt.deserialize([1, None, 2, 3])
print(Solution().preorder_traversal(t_root))
