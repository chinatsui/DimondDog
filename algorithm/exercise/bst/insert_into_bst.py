"""
LeetCode-701

Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5

You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1  3  5

This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""
from algorithm.core.binary_tree import TreeNode


class Solution1(object):

    def insert_into_bst(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert_into_bst(root.left, val)
        else:
            root.right = self.insert_into_bst(root.right, val)

        return root


class Solution2(object):

    @staticmethod
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)

        cur = root
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                else:
                    cur = cur.left
            elif val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                else:
                    cur = cur.right
            else:
                return root
