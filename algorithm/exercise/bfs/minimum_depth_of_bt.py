"""
LeetCode-111

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.
"""


class Solution:
    @staticmethod
    def min_depth(root):
        if root is None:
            return 0

        depth = 0
        q = [root]
        while q:
            depth += 1
            tmp = []
            for node in q:
                if node is None:
                    continue

                left = node.left
                right = node.right

                if left is None and right is None:
                    return depth

                tmp.append(left)
                tmp.append(right)
            q = tmp

        return depth
