class Solution:
    # @param root, a tree link node
    # @return nothing
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
