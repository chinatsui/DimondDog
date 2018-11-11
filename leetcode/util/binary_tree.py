def _is_leaf(node):
    return True if node is None else node.left is None and node.right is None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:

    @staticmethod
    def levelorder_traverse(root):
        """
        Actually, level order is a standard BFS
        """
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return res

    @staticmethod
    def preorder_traverse(root):
        """
        Actually, preorder is a standard DFS
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return res

    @staticmethod
    def inorder_traverse(root):
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res

    @staticmethod
    def postorder_traverse(root):
        res = []
        stack = []
        while root or stack:
            while not _is_leaf(root):
                stack.append(root)
                root = root.left

            if root:
                res.append(root.val)

            while stack and stack[-1].right == root:
                root = stack.pop()
                res.append(root.val)

            if stack:
                root = stack[-1].right
            else:
                root = None
        return res;

    @staticmethod
    def deserialize(data):
        if not data or not data[0]:
            return None

        root = TreeNode(data.pop(0))
        q = [root]
        while q:
            cur = q.pop(0)

            left_val = data.pop(0) if data else None
            if left_val is not None:
                cur.left = TreeNode(left_val)
                q.append(cur.left)

            right_val = data.pop(0) if data else None
            if right_val is not None:
                cur.right = TreeNode(right_val)
                q.append(cur.right)
        return root

    @staticmethod
    def serialize(root):
        if not root:
            return None

        res = []
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur:
                res.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append(None)
        return res


class InorderIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def has_next(self):
        return True if self.stack else False

    def next(self):
        node = self.stack.pop()
        res = node.val
        while node:
            self.stack.append(node)
            node = node.left
        return res


class PreorderIterator:
    def __init__(self, root):
        self.stack = [root]

    def has_next(self):
        return True if self.stack else False

    def next(self):
        node = self.stack.pop()

        if node.right:
            self.stack.append(node.right)

        if node.left:
            self.stack.append(node.left)

        return node.val


def test_binary_tree_levelorder_traverse():
    t_root = BinaryTree.deserialize([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, 9])
    print(BinaryTree.levelorder_traverse(t_root))


def test_binary_tree_preorder_traverse():
    t_root = BinaryTree.deserialize([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, 9])
    print(BinaryTree.preorder_traverse(t_root))


def test_binary_tree_inorder_traverse():
    t_root = BinaryTree.deserialize([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, 9])
    print(BinaryTree.inorder_traverse(t_root))


def test_binary_tree_postorder_traverse():
    t_root = BinaryTree.deserialize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(BinaryTree.postorder_traverse(t_root))


def test_preorder_iterator():
    t_res = []
    t_root = BinaryTree.deserialize([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, 9])
    preorder_itr = PreorderIterator(t_root)
    while preorder_itr.has_next():
        t_res.append(preorder_itr.next())
    print(t_res)


def test_inorder_iterator():
    t_res = []
    t_root = BinaryTree.deserialize([2, 1])
    inorder_itr = InorderIterator(t_root)
    while inorder_itr.has_next():
        t_res.append(inorder_itr.next())
    print(t_res)


test_binary_tree_levelorder_traverse()
# test_binary_tree_preorder_traverse()
# test_binary_tree_inorder_traverse()
# test_binary_tree_postorder_traverse()
# test_preorder_iterator()
# test_inorder_iterator()
