"""
LeetCode-124

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


class Solution:

    def max_path_sum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('-inf')]
        self._traverse(root, res)
        return res[0]

    def _traverse(self, node, res):
        if not node:
            return 0

        left_sum = max(0, self._traverse(node.left, res))
        right_sum = max(0, self._traverse(node.right, res))

        tmp = node.val + left_sum + right_sum
        res[0] = max(tmp, res[0])
        return max(left_sum, right_sum) + node.val
