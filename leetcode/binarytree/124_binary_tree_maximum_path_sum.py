class Solution:

    def max_path_sum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('-inf')]
        self._traverse(root, res)
        return res[0]

    def _traverse(self, node, res):
        if not node:
            return 0

        left_sum = max(0, self._traverse(node.left, res))
        right_sum = max(0, self._traverse(node.right, res))

        tmp = node.val + left_sum + right_sum
        res[0] = max(tmp, res[0])
        return max(left_sum, right_sum) + node.val
