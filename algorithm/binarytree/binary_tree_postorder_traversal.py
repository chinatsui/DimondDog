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
from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    def postorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or stack:
            while not self.isLeaf(root):
                stack.append(root)
                root = root.left

            if root:
                res.append(root.val)

            while stack and stack[-1].right == root:
                root = stack.pop()
                res.append(root.val)

            if stack:
                root = stack[-1].right
            else:
                root = None
        return res;

    @staticmethod
    def isLeaf(node):
        return True if node is None else node.left is None and node.right is None


t_root = bt.deserialize([1, None, 2, 3])
t_res = Solution().postorder_traversal(t_root)
print(t_res)
