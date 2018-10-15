from leetcode.util.binary_tree import BinaryTree as bt


class Solution:
    def is_symmetric(self, root):
        if root is None:
            return True
        return self._compare(root.left, root.right)

    def _compare(self, left, right):
        if left is None and right is None:
            return True

        if left and right:
            return left.val == right.val \
                   and self._compare(left.left, right.right) \
                   and self._compare(left.right, right.left)

        return False


t_root = bt.deserialize([1, 2, 2, 3, 4, 4, 3])
print(Solution().is_symmetric(t_root))
