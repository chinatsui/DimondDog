"""
LeetCode-450

Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


class Solution1:
    def delete_node(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            min_val = self._find_min_val(root.right)
            root.val = min_val
            root.right = self.delete_node(root.right, min_val)
        return root

    @staticmethod
    def _find_min_val(node):
        while node.left:
            node = node.left
        return node.val


class Solution2:
    @staticmethod
    def delete_node(root, key):
        if not root:
            return root

        cur, parent = root, None

        while cur and cur.val != key:
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if not cur:
            return root

        if cur.left and cur.right:
            _min, _min_parent = cur.right, cur
            while _min.left:
                _min_parent = _min
                _min = _min.left
            cur.val = _min.val
            cur = _min
            parent = _min_parent

        child = cur.left if cur.left else cur.right

        if not parent:
            return child
        elif parent.left == cur:
            parent.left = child
        else:
            parent.right = child

        return root
