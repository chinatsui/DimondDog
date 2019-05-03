"""
LeetCode-108

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from algorithm.core.binary_tree import TreeNode


class Solution:
    def sorted_array_to_bst(self, nums):
        if not nums:
            return None

        return self._construct(nums, 0, len(nums) - 1)

    def _construct(self, nums, lo, hi):
        if lo > hi:
            return None

        if lo == hi:
            return TreeNode(nums[lo])

        mi = lo + (hi - lo) // 2

        root = TreeNode(nums[mi])
        root.left = self._construct(nums, lo, mi - 1)
        root.right = self._construct(nums, mi + 1, hi)

        return root
