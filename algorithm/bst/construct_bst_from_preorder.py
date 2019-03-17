"""
LeetCode-1008

Return the root node of a binary search tree that matches the given preorder traversal.
"""
from algorithm.util.binary_tree import BinaryTree, TreeNode


class Solution:
    def bst_from_preorder(self, preorder) -> TreeNode:
        return self._construct(preorder, 0, len(preorder) - 1)

    def _construct(self, preorder, lo, hi):
        if lo > hi:
            return None

        if lo == hi:
            return TreeNode(preorder[lo])

        root = TreeNode(preorder[lo])
        pivot = lo
        for i in range(lo + 1, hi + 1):
            if preorder[i] > preorder[pivot]:
                pivot = i
                break

        if pivot == lo:
            root.left = self._construct(preorder, pivot + 1, hi)
        else:
            root.left = self._construct(preorder, lo + 1, pivot - 1)
            root.right = self._construct(preorder, pivot, hi)

        return root


t_root = Solution().bst_from_preorder([8, 5, 1, 7, 10, 12])
print(BinaryTree.serialize(t_root))
