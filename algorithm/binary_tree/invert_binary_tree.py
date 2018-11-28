"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left

        return root
