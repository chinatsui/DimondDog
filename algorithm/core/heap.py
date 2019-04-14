class MinHeap:

    def __init__(self):
        self.nums = []

    def offer(self, num):
        self.nums.append(num)
        self._swim(self.size() - 1)

    def poll(self):
        self._swap(0, -1)
        res = self.nums.pop()
        self._sink(0)
        return res

    def size(self):
        return len(self.nums)

    def _swap(self, src, dst):
        self.nums[src], self.nums[dst] = self.nums[dst], self.nums[src]

    def _swim(self, idx):
        if not idx:
            return

        p_idx = (idx - 1) // 2
        if self.nums[idx] < self.nums[p_idx]:
            self._swap(p_idx, idx)
            self._swim(p_idx)

    def _sink(self, idx):
        l_idx = (idx + 1) * 2 - 1
        r_idx = (idx + 1) * 2
        bound = self.size() - 1

        if r_idx <= bound:
            if self.nums[l_idx] <= self.nums[r_idx] and self.nums[idx] > self.nums[l_idx]:
                self._swap(idx, l_idx)
                self._sink(l_idx)
            elif self.nums[r_idx] <= self.nums[l_idx] and self.nums[idx] > self.nums[r_idx]:
                self._swap(idx, r_idx)
                self._sink(r_idx)
        elif l_idx <= bound:
            if self.nums[idx] > self.nums[l_idx]:
                self._swap(idx, l_idx)


t_min_heap = MinHeap()
t_min_heap.offer(5)
t_min_heap.offer(15)
t_min_heap.offer(9)
t_min_heap.offer(22)
t_min_heap.offer(11)
t_min_heap.offer(2)

while t_min_heap.size():
    print(t_min_heap.poll())
