"""
LeetCode-285

In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree.
Inorder Successor is NULL for the last node in Inorder traversal.

In Binary Search Tree, Inorder Successor of an input node can also be defined as the node with the smallest key greater
than the key of input node. So, it is sometimes important to find next node in sorted order.

             20
            /  \
           8   22
          / \
         4  12
           /  \
          10  14

In the above diagram, inorder successor of 8 is 10, inorder successor of 10 is 12 and inorder successor of 14 is 20.
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution:

    def inorder_successor(self, root, val):
        if not root:
            return None

        stack = []
        self.push_nodes(stack, root)
        while stack:
            node = stack.pop()
            self.push_nodes(stack, node.right)
            if node.val == val:
                return stack[-1].val
        return None

    @staticmethod
    def push_nodes(stack, node):
        while node:
            stack.append(node)
            node = node.left


t_root = bt.deserialize([20, 8, 22, 4, 12, None, None, None, None, 10, 14])
print(Solution().inorder_successor(t_root, 8))
