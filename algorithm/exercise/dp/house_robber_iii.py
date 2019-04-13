"""
LeetCode-337

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:

    def rob(self, root):
        cache = dict()
        return max(self._dfs(root, True, cache), self._dfs(root, False, cache))

    def _dfs(self, node, include, cache):
        if not node:
            return 0

        key = (node, include)
        if key in cache:
            return cache[key]

        if include:
            sum = node.val
            sum += self._dfs(node.left, False, cache)
            sum += self._dfs(node.right, False, cache)
            cache[key] = sum
            return sum
        else:
            sum1 = self._dfs(node.left, True, cache) + self._dfs(node.right, True, cache)
            sum2 = self._dfs(node.left, True, cache) + self._dfs(node.right, False, cache)
            sum3 = self._dfs(node.left, False, cache) + self._dfs(node.right, True, cache)
            sum4 = self._dfs(node.left, False, cache) + self._dfs(node.right, False, cache)
            sum = max(sum1, sum2, sum3, sum4)
            cache[key] = sum
            return sum


class Solution2:
    def rob(self, root):
        return self._dfs(root, {})

    def _dfs(self, node, cache):
        if not node:
            return 0

        if node in cache:
            return cache[node]

        left, right = node.left, node.right

        way_1 = node.val
        if left:
            way_1 += self._dfs(left.left, cache) + self._dfs(left.right, cache)

        if right:
            way_1 += self._dfs(right.left, cache) + self._dfs(right.right, cache)

        way_2 = self._dfs(left, cache) + self._dfs(right, cache)

        res = max(way_1, way_2)
        cache[node] = res
        return res

# t_root = bt.deserialize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# print(Solution().rob(t_root))
# print(Solution2().rob(t_root))
