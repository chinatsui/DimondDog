"""
LeetCode-112

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == sum
        else:
            sum -= root.val
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


t_root = bt.deserialize([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
t_res = Solution().hasPathSum(t_root, 22)
print(t_res)
