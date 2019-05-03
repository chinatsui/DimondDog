"""
LeetCode-116

Given a binary tree

TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (all leaves are at the same level, and every parent has two children).

Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7

After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""


class Solution:
    @staticmethod
    def connect(root):
        head = root
        while head:
            root = head
            while root:
                if root.left:
                    root.left.next = root.right
                    if root.next:
                        root.right.next = root.next.left
                root = root.next
            head = head.left
        return root


class Solution2(object):
    @staticmethod
    def connect(root):
        head = root
        while head:
            prev, cur = None, head
            while cur and cur.left:
                cur.left.next = cur.right
                if prev:
                    prev.right.next = cur.left
                prev = cur
                cur = cur.next
            head = head.left
        return root
