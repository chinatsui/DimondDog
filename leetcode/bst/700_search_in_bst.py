class Solution(object):
    def search_in_bst(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val == root.val:
            return root
        elif val < root.val and root.left:
            return self.search_in_bst(root.left, val)
        elif val > root.val and root.right:
            return self.search_in_bst(root.right, val)
        else:
            return None
