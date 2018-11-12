class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            min_val = self._find_min_val(root.right)
            root.val = min_val
            root.right = self.deleteNode(root.right, min_val)
        return root

    @staticmethod
    def _find_min_val(node):
        while node.left:
            node = node.left
        return node.val
