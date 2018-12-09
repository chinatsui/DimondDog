"""
Given a binary tree, find the length of the longest path where each node in the path has the same value.
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2


Example 2:
Input:
              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

"""

from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    """
    This problem is very similar to BinaryTreeMaximumPathSum.
    """

    def __init__(self):
        self.res = 0

    def longest_uni_value_path(self, root):
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0

        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0

        self.res = max(self.res, left + right)

        return max(left, right)


t_root = bt.deserialize([1, 4, 5, 4, 4, None, 5])
print(Solution().longest_uni_value_path(t_root))
