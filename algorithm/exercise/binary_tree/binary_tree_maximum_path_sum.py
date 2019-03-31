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
    """
    This problem is very similar to LongestUniValuePath.
    """

    def __init__(self):
        self.res = float('-inf')

    def max_path_sum(self, root):
        self._dfs(root)
        return self.res

    def _dfs(self, node):
        if not node:
            return 0

        left_val = max(0, self._dfs(node.left))
        right_val = max(0, self._dfs(node.right))

        tmp = node.val + left_val + right_val
        self.res = max(tmp, self.res)
        return max(left_val, right_val) + node.val
