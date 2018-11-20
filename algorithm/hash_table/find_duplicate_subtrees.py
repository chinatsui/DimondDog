"""
LeetCode-652

Given a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4

Therefore, you need to return above trees' root in the form of a list.
"""
from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    def find_duplicate_subtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        track_set = set()
        res_map = dict()
        self._traverse(root, track_set, res_map)
        return [node for (track, node) in res_map.items()]

    def _traverse(self, node, track_set, res_map):
        if not node:
            return 'N'
        else:
            track = str(node.val)
            track += self._traverse(node.left, track_set, res_map)
            track += self._traverse(node.right, track_set, res_map)
            if track in track_set:
                res_map[track] = node
            else:
                track_set.add(track)
            return track


t_root = bt.deserialize([1, 2, 3, 4, None, 2, 4, None, None, 4])
print(Solution().find_duplicate_subtrees(t_root))
