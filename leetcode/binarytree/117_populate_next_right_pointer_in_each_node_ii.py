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
