from leetcode.util.binary_tree import TreeNode


class Solution(object):

    def insert_into_bst(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert_into_bst(root.left, val)
        else:
            root.right = self.insert_into_bst(root.right, val)

        return root
