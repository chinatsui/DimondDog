"""
LeetCode-236

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
from algorithm.core.binary_tree import BinaryTree as bt
from algorithm.core.binary_tree import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        to_from = {}
        self._dfs(root, to_from)
        p_path = self._path_to(root, p, to_from)
        q_path = self._path_to(root, q, to_from)

        for p_node in p_path:
            for q_node in q_path:
                if p_node == q_node:
                    return p_node

    def _dfs(self, node, to_from):
        if node is None:
            return

        if node.left:
            to_from[node.left] = node
            self._dfs(node.left, to_from)

        if node.right:
            to_from[node.right] = node
            self._dfs(node.right, to_from)

    @staticmethod
    def _path_to(root, node, to_from):
        path = []
        while node != root:
            path.append(node)
            node = to_from[node]
        path.append(root)
        return path


t_root = bt.deserialize([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
t_root = TreeNode(3)
t_root.left = TreeNode(5)
t_root.right = TreeNode(1)
t_root.left.left = TreeNode(6)
t_root.left.right = TreeNode(2)
t_root.right.left = TreeNode(0)
t_root.right.right = TreeNode(8)
t_root.left.right.left = TreeNode(7)
t_root.left.right.right = TreeNode(4)

p = t_root.left
q = t_root.left.right.right

print(Solution().lowestCommonAncestor(t_root, p, q).val)
