"""
LeetCode-99

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]
   1
  /
 3
  \
   2

Output: [3,1,null,null,2]
   3
  /
 1
  \
   2


Example 2:
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""
from algorithm.core.binary_tree import TreeNode


class Solution:

    def __init__(self):
        self.prev = TreeNode(float('-inf'))
        self.large = None
        self.small = None

    def recover_tree(self, root):
        self._traverse(root)
        self.large.val, self.small.val = self.small.val, self.large.val

    def _traverse(self, node):
        if not node:
            return

        self._traverse(node.left)

        if not self.large and self.prev.val > node.val:
            self.large = self.prev

        if self.large and self.prev.val > node.val:
            self.small = node

        self.prev = node
        self._traverse(node.right)
