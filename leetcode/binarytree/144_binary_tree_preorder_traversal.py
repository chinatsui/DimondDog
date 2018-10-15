from leetcode.util.binary_tree import BinaryTree as bt


class Solution:
    def preorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or stack:
            while not self.isLeaf(root):
                res.append(root.val)
                stack.append(root)
                root = root.left

            if root:
                res.append(root.val)

            while stack and stack[-1].right == root:
                root = stack.pop()

            if stack:
                root = stack[-1].right
            else:
                root = None
        return res

    @staticmethod
    def isLeaf(node):
        return True if node is None else node.left is None and node.right is None


t_root = bt.deserialize([1, None, 2, 3])
t_res = Solution().preorder_traversal(t_root)
print(t_res)
