"""
LeetCode-98

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""


class Solution1:
    def is_valid_bst(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        track = None
        stack = []
        while root or stack:
            while not self._is_leaf(root):
                stack.append(root)
                root = root.left

            if root:
                if track is None or track < root.val:
                    track = root.val
                else:
                    return False

            while stack and stack[-1].right == root:
                root = stack.pop()

            if stack:
                if track is None or track < stack[-1].val:
                    track = stack[-1].val
                else:
                    return False
                root = stack[-1].right
            else:
                root = None
        return True

    @staticmethod
    def _is_leaf(node):
        return True if node is None else node.left is None and node.right is None


class Solution2:
    def is_valid_bst(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._traverse_check(root)

    def _traverse_check(self, node, min=float('-inf'), max=float('inf')):
        if node is None:
            return True

        if min >= node.val or max <= node.val:
            return False

        return self._traverse_check(node.left, min, node.val) and self._traverse_check(node.right, node.val, max)