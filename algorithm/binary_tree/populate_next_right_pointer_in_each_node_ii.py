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
    """
    In contrast to LeetCode-116, we need to additionally maintain a child_cur for link operation.
    Besides, it is a bit more complicated to find the next head, think it over for all kinds of cases.
    """

    @staticmethod
    def connect(root):
        head = root
        while head:
            cur = head
            child_cur = None

            if head.left:
                head = head.left
            else:
                head = head.right

            while cur:
                if cur.left:
                    child_cur = cur.left
                    if cur.right:
                        child_cur.next = cur.right
                        child_cur = child_cur.next
                elif cur.right:
                    child_cur = cur.right

                if cur.next:
                    if child_cur:
                        if cur.next.left:
                            child_cur.next = cur.next.left
                            child_cur = child_cur.next
                        elif cur.next.right:
                            child_cur.next = cur.next.right
                            child_cur = child_cur.next
                cur = cur.next
                if not head and cur:
                    if cur.left:
                        head = cur.left
                    else:
                        head = cur.right
