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
from algorithm.util.binary_tree import BinaryTree as bt


class Solution:
    @staticmethod
    def level_order_traversal(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root:
            q = [(0, root)]
            while q:
                (cur_level, cur_node) = q.pop(0)

                if cur_level >= len(res):
                    cur_list = []
                    res.append(cur_list)
                else:
                    cur_list = res[cur_level]

                cur_list.append(cur_node.val)

                if cur_node.left:
                    q.append((cur_level + 1, cur_node.left))

                if cur_node.right:
                    q.append((cur_level + 1, cur_node.right))
        return res


class Solution1:

    @staticmethod
    def traverse(root):
        res = []
        q = [root]
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
t_res = Solution1.traverse(t_root)
print(t_res)
