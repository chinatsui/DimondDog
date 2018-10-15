from leetcode.util.binary_tree import BinaryTree as bt


class Solution:
    def inorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or stack:
            while not self.is_leaf(root):
                stack.append(root)
                root = root.left

            if root:
                res.append(root.val)

            while stack and stack[-1].right == root:
                root = stack.pop()

            if stack:
                res.append(stack[-1].val)
                root = stack[-1].right
            else:
                root = None
        return res

    @staticmethod
    def is_leaf(node):
        if node:
            return node.left is None and node.right is None
        else:
            return True


t_root = bt.deserialize([1, None, 2, 3])
t_res = Solution().inorder_traversal(t_root)
print(t_res)
