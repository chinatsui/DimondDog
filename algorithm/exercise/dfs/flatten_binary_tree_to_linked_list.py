"""
LeetCode-114

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
from algorithm.core.binary_tree import BinaryTree


class Solution:
    """
    My initial implementation is to flatten the tree to below format:
                        1
                       /
                      2
                     /
                    3
                   /
                  4
                 /
                5
               /
              6
    Although it is a linked list, but not expected as requirement.
    Think the answer over and over.
    Besides, this problem is a very good example to recurse and change a tree in-place.
    """

    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            cur = root.left
            while cur.right:
                cur = cur.right
            cur.right = root.right
            root.right = root.left
            root.left = None


t_root = BinaryTree.deserialize([1, 2, 5, 3, 4, None, 6])
Solution().flatten(t_root)
print(BinaryTree.serialize(t_root))
