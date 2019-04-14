def swap(nums, src, dst):
    nums[src], nums[dst] = nums[dst], nums[src]


class QuickSort:
    def sort(self, nums):
        if not nums:
            return

        left, right = 0, len(nums) - 1
        self._partition(nums, left, right)

    def _partition(self, nums, left, right):
        if left >= right:
            return
        pivot = right
        sm = left - 1
        for i in range(left, right):
            if nums[i] < nums[pivot]:
                sm += 1
                swap(nums, sm, i)

        swap(nums, sm + 1, pivot)
        pivot = sm + 1
        self._partition(nums, left, sm)
        self._partition(nums, pivot + 1, right)


class QuickSort2:
    @staticmethod
    def sort(nums):
        if not nums:
            return

        q = [0, len(nums) - 1]
        while q:
            left = q.pop(0)
            right = q.pop(0)

            if left >= right:
                continue

            pivot = right
            sm = left - 1
            for i in range(left, right):
                if nums[i] < nums[pivot]:
                    sm += 1
                    swap(nums, sm, i)
            swap(nums, sm + 1, pivot)
            pivot = sm + 1
            q.append(left)
            q.append(sm)
            q.append(pivot + 1)
            q.append(right)


class MergeSort:
    def sort(self, nums):
        if not nums:
            return

        left = 0
        right = len(nums) - 1
        self._sort(nums, left, right)

    def _sort(self, nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self._sort(nums, left, mid)
        self._sort(nums, mid + 1, right)
        self._merge(nums, left, mid, right)

    @staticmethod
    def _merge(nums, left, mid, right):
        aux = nums[:]
        m, n = left, mid + 1
        for i in range(left, right + 1):
            if m > mid:  # left is over
                nums[i] = aux[n]
                n += 1
            elif n > right:  # right is over
                nums[i] = aux[m]
                m += 1
            elif aux[m] < aux[n]:
                nums[i] = aux[m]
                m += 1
            else:
                nums[i] = aux[n]
                n += 1


class MergeSort2:
    def sort(self, nums):
        if not nums:
            return

        size = len(nums)
        i = 1
        while i < size:
            left = 0
            while left + i - 1 < size:
                mid = left + i - 1
                right = mid + i
                if right >= size:
                    right = size - 1
                self._merge(nums, left, mid, right)
                left += 2 * i
            i *= 2

    @staticmethod
    def _merge(nums, left, mid, right):
        aux = nums[:]

        m, n = left, mid + 1
        for i in range(left, right + 1):
            if m > mid:
                nums[i] = aux[n]
                n += 1
            elif n > right:
                nums[i] = aux[m]
                m += 1
            elif aux[m] < aux[n]:
                nums[i] = aux[m]
                m += 1
            else:
                nums[i] = aux[n]
                n += 1


class HeapSort:
    def sort(self, nums):
        if not nums:
            return

        self._heapify(nums)
        tail = len(nums) - 1
        while tail:
            swap(nums, 0, tail)
            self._sink(nums, 0, tail - 1)
            tail -= 1

    def _heapify(self, nums):
        n = len(nums)
        i = n // 2 - 1
        while i > 0:
            self._sink(nums, i, n - 1)
            i -= 1

    def _sink(self, nums, idx, bound):
        l_idx = (idx + 1) * 2 - 1
        r_idx = (idx + 1) * 2

        if r_idx <= bound:
            if nums[l_idx] <= nums[r_idx] and nums[idx] < nums[r_idx]:
                swap(nums, idx, r_idx)
                self._sink(nums, r_idx, bound)
            elif nums[r_idx] <= nums[l_idx] and nums[idx] < nums[l_idx]:
                swap(nums, idx, l_idx)
                self._sink(nums, l_idx, bound)
        elif l_idx <= bound:
            if nums[idx] < nums[l_idx]:
                swap(nums, idx, l_idx)


class BubbleSort:
    @staticmethod
    def sort(nums):
        if not nums:
            return

        n = len(nums)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


class InsertionSort:

    @staticmethod
    def sort(nums):
        if not nums:
            return

        n = len(nums)
        for i in range(1, n):
            for j in range(i - n, -n, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]


t_nums = [25, 68, 68, 62, 68, 56, 30, 56,
          32, 64, 41, 6, 39, 19, 28, 46,
          11, 18, 53, 59, 11, 71, 73, 75,
          76, 80, 83, 85, 91, 99]
# QuickSort().sort(t_nums)
# MergeSort().sort(t_nums)
# QuickSort2().sort(t_nums)
# MergeSort2().sort(t_nums)
# HeapSort().sort(t_nums)
# BubbleSort().sort(t_nums)
# InsertionSort().sort(t_nums)
# print(t_nums)
