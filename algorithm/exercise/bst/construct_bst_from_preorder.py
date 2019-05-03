"""
LeetCode-1008

Return the root node of a binary search tree that matches the given preorder traversal.
"""
from algorithm.core.binary_tree import BinaryTree, TreeNode


class Solution:
    def bst_from_preorder(self, preorder) -> TreeNode:
        return self._construct(preorder, 0, len(preorder) - 1)

    def _construct(self, preorder, lo, hi):
        if lo > hi:  # left child is None
            return None

        root = TreeNode(preorder[lo])

        if lo == hi:
            return root

        pi = lo
        for i in range(lo + 1, hi + 1):
            if preorder[i] > preorder[pi]:
                pi = i
                break

        if pi == lo:  # right child is None
            root.left = self._construct(preorder, pi + 1, hi)
        else:
            root.left = self._construct(preorder, lo + 1, pi - 1)
            root.right = self._construct(preorder, pi, hi)

        return root


t_root = Solution().bst_from_preorder([8, 5, 1, 7, 10, 12])
print(BinaryTree.serialize(t_root))
