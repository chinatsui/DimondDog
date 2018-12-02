"""
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
from algorithm.util.binary_tree import TreeNode


class Solution:

    def __init__(self):
        self.prev = TreeNode(float('-inf'))
        self.first = None
        self.second = None

    def recoverTree(self, root):
        self._traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def _traverse(self, node):
        if not node:
            return

        self._traverse(node.left)

        if not self.first and self.prev.val > node.val:
            self.first = self.prev

        if self.first and self.prev.val > node.val:
            self.second = node

        self.prev = node
        self._traverse(node.right)
