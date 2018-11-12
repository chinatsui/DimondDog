class Solution1:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left_depth = self._dfs_depth(root.left, 0)
        right_depth = self._dfs_depth(root.right, 0)

        diff = abs(left_depth - right_depth)
        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)

        if diff <= 1 and is_left_balanced and is_right_balanced:
            return True
        else:
            return False

    def _dfs_depth(self, node, depth):
        if not node:
            return depth

        left_depth = self._dfs_depth(node.left, depth + 1)
        right_depth = self._dfs_depth(node.right, depth + 1)
        return max(left_depth, right_depth)


class Solution2:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if self._dfs_height(root) != -1 else False

    def _dfs_height(self, node):
        if not node:
            return 0

        left_height = self._dfs_height(node.left)
        if left_height == -1:
            return -1

        right_height = self._dfs_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1
