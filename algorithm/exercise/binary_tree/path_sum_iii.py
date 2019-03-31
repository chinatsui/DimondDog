"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:

    def path_sum(self, root, sum):
        cache = dict()
        cache[0] = 1
        return self._dfs(root, 0, sum, cache)

    def _dfs(self, node, cur_sum, sum, cache):
        if not node:
            return 0

        cur_sum += node.val
        cnt = cache.get(cur_sum - sum, 0)

        cache[cur_sum] = cache.get(cur_sum, 0) + 1
        cnt += self._dfs(node.left, cur_sum, sum, cache)
        cnt += self._dfs(node.right, cur_sum, sum, cache)
        cache[cur_sum] -= 1
        return cnt


t_root = bt.deserialize([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
print(Solution().path_sum(t_root, 8))
