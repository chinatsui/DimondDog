from collections import Counter
from queue import PriorityQueue


class Solution:
    @staticmethod
    def top_k_frequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = Counter(n for n in nums)
        pq = PriorityQueue()
        for (n, count) in freq_map.items():
            pq.put((-count, n))

        return [pq.get()[1] for _ in range(k)]


print(Solution().top_k_frequent([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5], 2))
