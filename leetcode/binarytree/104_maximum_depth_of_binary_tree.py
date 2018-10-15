from leetcode.util.binary_tree import BinaryTree as bt


class Solution:
    def max_depth(self, root):
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


t_root = bt.deserialize([3, 9, 20, None, None, 15, 7])
t_res = Solution().max_depth(t_root)
print(t_res)
