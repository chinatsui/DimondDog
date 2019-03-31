"""
Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Output: [9, 3, 15, 20, 7]
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:

    def column_traversal(self, root):
        column_map = dict()
        self._dfs(root, 0, column_map)
        res = [nodes for (x, nodes) in sorted(column_map.items())]
        return res

    def _dfs(self, node, x, column_map):
        if not node:
            return

        if x in column_map:
            column_map[x].append(node.val)
        else:
            column_map[x] = [node.val]

        self._dfs(node.left, x - 1, column_map)
        self._dfs(node.right, x + 1, column_map)


t_root = bt.deserialize([3, 9, 20, None, None, 15, 7])
print(Solution().column_traversal(t_root))
