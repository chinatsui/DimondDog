"""
LeetCode-145

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    def postorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        self._push_nodes(stack, root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if stack and node == stack[-1].left:
                node = stack[-1].right
                self._push_nodes(stack, node)
        return res

    @staticmethod
    def _push_nodes(stack, node):
        while node:
            stack.append(node)
            if node.left:
                node = node.left
            else:
                node = node.right


t_root = bt.deserialize([1, None, 2, 3])
t_res = Solution().postorder_traversal(t_root)
print(t_res)
