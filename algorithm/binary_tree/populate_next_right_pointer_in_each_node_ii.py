"""
LeetCode-117

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
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
"""
from collections import deque


class Solution:
    def connect(self, root):
        if not root:
            return

        q = deque()
        cur = (0, root)
        while cur or q:
            nxt = q.popleft() if q else None
            if nxt and cur[0] == nxt[0]:
                cur[1].next = nxt[1]
            self.add_children(q, cur[0], cur[1])
            cur = nxt if nxt else q.popleft() if q else None

    def add_children(self, q, level, node):
        if node.left:
            q.append((level + 1, node.left))

        if node.right:
            q.append((level + 1, node.right))
