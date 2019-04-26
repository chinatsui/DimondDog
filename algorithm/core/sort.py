def swap(nums, src, dst):
    nums[src], nums[dst] = nums[dst], nums[src]


def merge(nums, lo, mi, hi):
    aux = nums[:]

    left, right = lo, mi + 1
    for i in range(lo, hi + 1):
        if left > mi:
            nums[i] = aux[right]
            right += 1
        elif right > hi:
            nums[i] = aux[left]
            left += 1
        elif aux[left] <= aux[right]:
            nums[i] = aux[left]
            left += 1
        else:
            nums[i] = aux[right]
            right += 1


class QuickSort:
    """
    O(N*logN), in-place, unstable sorting algorithm
    """

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
    """
    O(N*logN), in-place, unstable sorting algorithm
    """

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
    """
    O(N*logN), non in-place, stable sorting algorithm
    """

    def sort(self, nums):
        if not nums:
            return

        self._sort(nums, 0, len(nums) - 1)

    def _sort(self, nums, lo, hi):
        if lo >= hi:
            return

        mi = (lo + hi) // 2
        self._sort(nums, lo, mi)
        self._sort(nums, mi + 1, hi)
        merge(nums, lo, mi, hi)


class MergeSort2:
    """
    O(N*logN), non in-place, stable sorting algorithm
    """

    def sort(self, nums):
        if not nums:
            return

        n = len(nums)
        i = 1
        while i < n:
            lo = 0
            while lo + i - 1 < n:
                mi = lo + i - 1
                hi = mi + i
                if hi >= n:
                    hi = n - 1
                merge(nums, lo, mi, hi)
                lo = hi + 1
            i *= 2


class HeapSort:
    """
    O(N*logN), in-place, unstable sorting algorithm
    """

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
    """
    O(N^2), in-place, stable soring algorithm
    """

    @staticmethod
    def sort(nums):
        if not nums:
            return

        n = len(nums)
        for i in range(n):
            is_sorted = True
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    is_sorted = False
                    swap(nums, j, j + 1)
            if is_sorted:
                break


class InsertionSort:
    """
    O(N^2), in-place, stable sorting algorithm
    """

    @staticmethod
    def sort(nums):
        if not nums:
            return

        n = len(nums)
        for i in range(1, n):
            for j in range(i - n, -n, -1):
                if nums[j] < nums[j - 1]:
                    swap(nums, j, j - 1)
                else:
                    break


class SelectionSort:
    """
    O(N^2), in-place, unstable sorting algorithm
    """

    @staticmethod
    def sort(nums):
        if not nums:
            return

        n = len(nums)
        for i in range(n):
            _min = i
            for j in range(i + 1, n):
                if nums[j] < nums[_min]:
                    _min = j
            swap(nums, i, _min)


class BucketSort:
    """
    O(N), not in-place, stable sorting algorithm
    """

    @staticmethod
    def sort(nums):
        """
        For convenience, assume all numbers in array are non negative numbers.
        """
        if not nums:
            return

        _max = max(nums)
        bucket = [[] for _ in range(_max + 1)]
        for num in nums:
            bucket[num].append(num)

        i = 0
        for buc in bucket:
            if buc:
                for num in buc:
                    nums[i] = num
                    i += 1


class CountingSort:
    """
    O(N), not in-place, stable sorting algorithm
    """

    @staticmethod
    def sort(nums):
        """
        For convenience, assume all numbers in array are non negative numbers.
        """
        if not nums:
            return

        _max = max(nums)
        cnt_arr = [0 for _ in range(_max + 1)]

        for num in nums:
            cnt_arr[num] += 1

        for i in range(1, _max + 1):
            cnt_arr[i] += cnt_arr[i - 1]

        aux = nums[:]
        for i in range(-1, -len(aux) - 1, -1):
            num = aux[i]
            cnt = cnt_arr[num]
            nums[cnt - 1] = num
            cnt_arr[num] -= 1


t_nums = [25, 68, 62, 68, 56, 30, 56, 32, 64, 41, 6, 39, 19, 28, 46, 11, 18, 53, 11, 71, 73, 75, 76, 80, 83, 85, 91, 99]
# QuickSort().sort(t_nums)
# MergeSort().sort(t_nums)
# QuickSort2().sort(t_nums)
# MergeSort2().sort(t_nums)
# HeapSort().sort(t_nums)
# BubbleSort().sort(t_nums)
# InsertionSort().sort(t_nums)
# SelectionSort().sort(t_nums)
# BucketSort().sort(t_nums)
CountingSort().sort(t_nums)
print(t_nums)
