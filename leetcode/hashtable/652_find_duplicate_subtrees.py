from leetcode.util.binary_tree import BinaryTree as bt


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
