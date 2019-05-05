"""
LeetCode - 257
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
from algorithm.core.binary_tree import BinaryTree


class Solution:
    def binary_tree_paths(self, root):
        if not root:
            return []

        res = []
        self._dfs(root, res, '')
        return res

    def _dfs(self, node, res, cur):
        if not node.left and not node.right:
            res.append(cur + str(node.val))
            return

        if node.left:
            self._dfs(node.left, res, cur + str(node.val) + '->')

        if node.right:
            self._dfs(node.right, res, cur + str(node.val) + '->')


t_root = BinaryTree.deserialize([1, 2, 3, None, 5])
print(Solution().binary_tree_paths(t_root))
