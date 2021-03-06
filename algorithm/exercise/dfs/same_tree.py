"""
LeetCode-100

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


class Solution:
    """
    My first thought is to dfs the two trees and record each node val ('N' if node is None), then compare trace.
    This approach is fine, but required extra space. Below solution is also using DFS,
    but it doesn't require extra space, think it over and over.
    """

    def is_same_tree(self, p, q):
        if not p and not q:
            return True

        if p and q:
            return p.val == q.val \
                   and self.is_same_tree(p.left, q.left) \
                   and self.is_same_tree(p.right, q.right)

        return False
