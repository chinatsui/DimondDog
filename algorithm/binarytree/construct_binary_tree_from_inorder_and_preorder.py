"""
LeetCode-105

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given:

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from algorithm.util.binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder and inorder:
            return self._build(inorder, 0, len(inorder) - 1, preorder, 0)
        else:
            return None

    def _build(self, inorder, i_src, i_dst, preorder, p):
        if i_src > i_dst:
            return None

        if i_src == i_dst:
            return TreeNode(inorder[i_src]);

        root = TreeNode(preorder[p])

        v = -1
        for x in range(i_src, i_dst + 1):
            if inorder[x] == preorder[p]:
                v = x
                break

        root.left = self._build(inorder, i_src, v - 1, preorder, p + 1)
        root.right = self._build(inorder, v + 1, i_dst, preorder, p + v - i_src + 1)

        return root


t_inorder = [1, 2, 3, 4]
t_preorder = [3, 2, 4, 1]
t_root = Solution().buildTree(t_inorder, t_preorder)
