from leetcode.util.binary_tree import TreeNode


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            return self._build(inorder, 0, len(inorder) - 1, postorder, len(postorder) - 1)
        else:
            return None

    def _build(self, inorder, i_src, i_dst, postorder, p):
        if i_src > i_dst:
            return None

        if i_src == i_dst:
            return TreeNode(inorder[i_src])

        root = TreeNode(postorder[p])

        v = -1
        for x in range(i_src, i_dst + 1):
            if inorder[x] == postorder[p]:
                v = x
                break

        root.left = self._build(inorder, i_src, v - 1, postorder, p - 1 - i_dst + v)
        root.right = self._build(inorder, v + 1, i_dst, postorder, p - 1)

        return root


t_inorder = [1, 2, 3, 4]
t_postorder = [3, 2, 4, 1]
t_root = Solution().buildTree(t_inorder, t_postorder)
