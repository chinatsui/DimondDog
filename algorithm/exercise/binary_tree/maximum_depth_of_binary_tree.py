"""
LeetCode-104

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:
    def max_depth(self, root):
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


t_root = bt.deserialize([3, 9, 20, None, None, 15, 7])
t_res = Solution().max_depth(t_root)
print(t_res)
