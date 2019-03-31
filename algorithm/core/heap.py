class MinHeap:

    def __init__(self):
        self.data = []

    def offer(self, num):
        self.data.append(num)
        idx = len(self.data) - 1
        self._swim(idx)

    def poll(self):
        res = self.data[0]
        self._swap(0, len(self.data) - 1)
        self.data.pop()
        self._sink(0)
        return res

    def size(self):
        return len(self.data) - 1

    def _swap(self, src, dst):
        tmp = self.data[dst]
        self.data[dst] = self.data[src]
        self.data[src] = tmp

    def _swim(self, idx):
        if not idx:
            return
        p_idx = (idx - 1) // 2
        if self.data[idx] < self.data[p_idx]:
            self._swap(p_idx, idx)
            self._swim(p_idx)

    def _sink(self, idx):
        l_idx = (idx + 1) * 2 - 1
        r_idx = (idx + 1) * 2

        if l_idx > len(self.data) - 1:
            return

        if l_idx == len(self.data) - 1 or self.data[l_idx] < self.data[r_idx]:
            if self.data[idx] > self.data[l_idx]:
                self._swap(idx, l_idx)
                self._sink(l_idx)
        else:
            if self.data[idx] > self.data[r_idx]:
                self._swap(idx, r_idx)
                self._sink(r_idx)


t_min_heap = MinHeap()
t_min_heap.offer(5)
t_min_heap.offer(15)
t_min_heap.offer(9)
t_min_heap.offer(22)
t_min_heap.offer(11)
t_min_heap.offer(2)

while t_min_heap.size():
    print(t_min_heap.poll())
