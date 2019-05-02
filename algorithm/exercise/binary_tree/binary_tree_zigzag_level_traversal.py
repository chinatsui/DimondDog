"""
LeetCode-103

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
from collections import deque

from algorithm.core.binary_tree import BinaryTree as bt


class Solution:
    @staticmethod
    def zigzag_level_order(root):
        if not root:
            return []

        res, deq = [], deque([(root, 0)])
        while deq:
            (node, level) = deq.popleft()
            if level == len(res):
                res.append(deque())

            tmp = res[level]
            if level % 2 == 0:
                tmp.append(node.val)
            else:
                tmp.appendleft(node.val)

            if node.left:
                deq.append((node.left, level + 1))

            if node.right:
                deq.append((node.right, level + 1))

        return [list(deq) for deq in res]


t_root = bt.deserialize([3, 9, 20, None, None, 15, 7])
print(Solution().zigzag_level_order(t_root))
