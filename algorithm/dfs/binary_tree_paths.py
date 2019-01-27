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
from algorithm.util.binary_tree import BinaryTree


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self._dfs(root, '', res)
        return res

    def _dfs(self, node, cur, res):
        if node is None:
            return

        if node.left is None and node.right is None:
            res.append(cur + str(node.val))
            return

        nxt_cur = cur + str(node.val) + '->'
        self._dfs(node.left, nxt_cur, res)
        self._dfs(node.right, nxt_cur, res)


t_root = BinaryTree.deserialize([1, 2, 3, None, 5])
print(Solution().binaryTreePaths(t_root))
