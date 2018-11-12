from leetcode.util.binary_tree import BinaryTree as bt


class Solution:
    @staticmethod
    def inorder_traversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            res.append(node.val)
            cur = node.right
            while cur:
                stack.append(cur)
                cur = cur.left
        return res


t_root = bt.deserialize([1, None, 2, 3])
t_res = Solution().inorder_traversal(t_root)
print(t_res)
