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
from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    def preorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
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
t_res = Solution().preorder_traversal(t_root)
print(t_res)
