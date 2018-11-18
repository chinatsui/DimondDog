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
from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    @staticmethod
    def inorder_traversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            res.append(node.val)
            cur = node.right
            while cur:
                stack.append(cur)
                cur = cur.left
        return res


t_root = bt.deserialize([1, None, 2, 3])
t_res = Solution().inorder_traversal(t_root)
print(t_res)
