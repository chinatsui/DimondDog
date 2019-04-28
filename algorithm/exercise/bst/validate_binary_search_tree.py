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
    @staticmethod
    def is_valid_bst(root):
        if not root:
            return True

        s = []

        while root:
            s.append(root)
            root = root.left

        _min = float('-inf')
        while s:
            node = s.pop()
            if _min >= node.val:
                return False
            else:
                _min = node.val
            cur = node.right
            while cur:
                s.append(cur)
                cur = cur.left
        return True


class Solution2:
    def is_valid_bst(self, root):
        return self._traverse_check(root)

    def _traverse_check(self, node, _min=float('-inf'), _max=float('inf')):
        if not node:
            return True

        if node.val <= _min or node.val >= _max:
            return False

        return self._traverse_check(node.left, _min, node.val) and self._traverse_check(node.right, node.val, _max)
