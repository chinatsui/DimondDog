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


class Solution:
    def connect(self, root):
        if root is None:
            return

        q = []
        cur = (0, root)
        while cur or q:
            nxt = q.pop(0) if q else None
            if nxt is None:
                cur[1].next = None
            else:
                if cur[0] == nxt[0]:
                    cur[1].next = nxt[1]
                else:
                    cur[1].next = None
            self._enqueue_children(cur, q)
            cur = nxt if nxt else q.pop(0) if q else None

    @staticmethod
    def _enqueue_children(t, q):
        if t[1].left:
            q.append((t[0] + 1, t[1].left))
        if t[1].right:
            q.append((t[0] + 1, t[1].right))
