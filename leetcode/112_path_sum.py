from leetcode.util.binary_tree import BinaryTree as bt


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if self._is_leaf(root):
            return root.val == sum
        else:
            sum -= root.val
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def _is_leaf(self, node):
        return True if node is None else node.left is None and node.right is None


t_root = bt.deserialize([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
t_res = Solution().hasPathSum(t_root, 22)
print(t_res)
