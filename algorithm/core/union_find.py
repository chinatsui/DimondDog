class UF:

    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.count = n

    def count(self):
        return self.count

    def connected(self, v, w):
        return self.find(v) == self.find(w)

    def find(self, v):
        pass

    def union(self, v, w):
        pass


class QuickFindUF(UF):

    def find(self, v):
        return self.ids[v]

    def union(self, v, w):
        v_id = self.find(v)
        w_id = self.find(w)

        if v_id == w_id:
            return

        for i in range(len(self.ids)):
            if self.ids[i] == v_id:
                self.ids[i] = w_id
        self.count -= 1


class QuickUnionUF(UF):

    def find(self, v):
        while v != self.ids[v]:
            v = self.ids[v]
        return v

    def union(self, v, w):
        v_id = self.find(v)
        w_id = self.find(w)

        if v_id == w_id:
            return

        self.ids[v_id] = w_id
        self.count -= 1


class WeightedQuickUnionUF(UF):

    def __init__(self):
        self.sz = [1 for _ in range(self.count)]

    def find(self, v):
        while v != self.ids[v]:
            v = self.ids[v]
        return v

    def union(self, v, w):
        v_id = self.find(v)
        w_id = self.find(w)

        if v_id == w_id:
            return

        #  Put the small component to large component
        if self.sz[v_id] < self.sz[w_id]:
            self.ids[v_id] = w_id
            self.sz[w_id] += self.sz[v_id]
        else:
            self.ids[w_id] = v_id
            self.sz[v_id] += self.sz[w_id]

        self.count -= 1
