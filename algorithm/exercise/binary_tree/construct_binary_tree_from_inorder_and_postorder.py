"""
LeetCode-106

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given:
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from algorithm.core.binary_tree import TreeNode


class Solution:
    def build_tree(self, inorder, postorder):
        if inorder and postorder:
            return self._build(inorder, 0, len(inorder) - 1, postorder, len(postorder) - 1)
        else:
            return None

    def _build(self, inorder, i_src, i_dst, postorder, p):
        if i_src > i_dst:
            return None

        root = TreeNode(postorder[p])

        if i_src == i_dst:
            return root

        v = inorder.index(postorder[p])
        root.left = self._build(inorder, i_src, v - 1, postorder, p - 1 - i_dst + v)
        root.right = self._build(inorder, v + 1, i_dst, postorder, p - 1)
        return root


t_inorder = [1, 2, 3, 4]
t_postorder = [3, 2, 4, 1]
t_root = Solution().build_tree(t_inorder, t_postorder)
