"""
LeetCode - 199

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


class Solution:
    def right_side_view(self, root):
        res = []
        self._dfs(root, 0, res)
        return res

    def _dfs(self, node, depth, view):
        if not node:
            return

        if depth == len(view):
            view.append(node.val)

        self._dfs(node.right, depth + 1, view)
        self._dfs(node.left, depth + 1, view)
