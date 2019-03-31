"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


class Solution:

    def pathSum(self, root, sum):
        res = []
        self._dfs(root, sum, [], res)
        return res

    def _dfs(self, node, sum, cur, res):
        if not node:
            return

        if node.left is None and node.right is None:
            if node.val == sum:
                res.append(cur + [node.val])
            else:
                return

        self._dfs(node.left, sum - node.val, cur + [node.val], res)
        self._dfs(node.right, sum - node.val, cur + [node.val], res)
