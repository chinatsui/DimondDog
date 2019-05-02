"""
LeetCode-102

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from algorithm.core.binary_tree import BinaryTree as bt


class Solution1:

    @staticmethod
    def traverse(root):
        if not root:
            return []

        res, q = [], [root]
        while q:
            tmp = []
            cur = []
            for node in q:
                cur.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(cur)
            q = tmp
        return res


t_root = bt.deserialize([3, 9, 20, None, None, 15, 7])
print(Solution1.traverse(t_root))
