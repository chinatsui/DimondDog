class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:

    @staticmethod
    def deserialize(data):
        if data and data[0] is not None:
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
        else:
            return None

    @staticmethod
    def serialize(root):
        data = []
        if root:
            q = [root]
            while q:
                cur = q.pop(0)
                if cur:
                    data.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    data.append(None)
        return data


t_root = BinaryTree.deserialize([0, 0, 0, 0, None, None, 1, None, None, None, 2])
t_data = BinaryTree.serialize(t_root)
print(t_data)
