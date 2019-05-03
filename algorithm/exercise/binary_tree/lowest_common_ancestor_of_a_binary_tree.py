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


class Solution(object):
    def __init__(self):
        self.to_from = dict()

    def lowest_common_ancestor(self, root, p, q):
        if not root:
            return None

        self._dfs(root)

        path_to_p = self._path_to(p)
        path_to_q = self._path_to(q)

        for m in path_to_p:
            for n in path_to_q:
                if m == n:
                    return m

        return None

    def _dfs(self, node):
        if not node:
            return

        if node.left:
            self.to_from[node.left] = node
            self._dfs(node.left)

        if node.right:
            self.to_from[node.right] = node
            self._dfs(node.right)

    def _path_to(self, node):
        path = []
        while node:
            path.append(node)
            node = self.to_from.get(node)
        return path


class Solution2:
    """
    Very smart solution, think it over and over.
    """
    def lowest_common_ancestor(self, root, p, q):
        if root in (None, p, q):
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        return root if left and right else left or right
