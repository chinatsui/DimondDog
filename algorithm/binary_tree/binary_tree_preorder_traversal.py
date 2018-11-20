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
        res = []
        stack = []
        while root or stack:
            while not self.isLeaf(root):
                res.append(root.val)
                stack.append(root)
                root = root.left

            if root:
                res.append(root.val)

            while stack and stack[-1].right == root:
                root = stack.pop()

            if stack:
                root = stack[-1].right
            else:
                root = None
        return res

    @staticmethod
    def isLeaf(node):
        return True if node is None else node.left is None and node.right is None


t_root = bt.deserialize([1, None, 2, 3])
t_res = Solution().preorder_traversal(t_root)
print(t_res)
