class Solution1:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        track = None
        stack = []
        while root or stack:
            while not self._is_leaf(root):
                stack.append(root)
                root = root.left

            if root:
                if track is None or track < root.val:
                    track = root.val
                else:
                    return False

            while stack and stack[-1].right == root:
                root = stack.pop()

            if stack:
                if track is None or track < stack[-1].val:
                    track = stack[-1].val
                else:
                    return False
                root = stack[-1].right
            else:
                root = None
        return True

    @staticmethod
    def _is_leaf(node):
        return True if node is None else node.left is None and node.right is None


class Solution2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._traverse_check(root)

    def _traverse_check(self, node, min=float('-inf'), max=float('inf')):
        if node is None:
            return True

        if min >= node.val or max <= node.val:
            return False

        return self._traverse_check(node.left, min, node.val) and self._traverse_check(node.right, node.val, max)
