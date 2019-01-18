"""
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
    This approach is fine, but required extra space. Below solution is also using DFS, but it doesn't require extra space, 
    think it over and over.
    """
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p and q:
            if p.val != q.val:
                return False

            left_same = self.isSameTree(p.left, q.left)
            if not left_same:
                return False

            right_same = self.isSameTree(p.right, q.right)
            if not right_same:
                return False

            return True

        return False
