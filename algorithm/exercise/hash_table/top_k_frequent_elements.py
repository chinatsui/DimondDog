"""
LeetCode-347

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
from queue import PriorityQueue


class Solution:
    @staticmethod
    def top_k_frequent(nums, k):
        freq_map = Counter(n for n in nums)
        pq = PriorityQueue()
        for (n, count) in freq_map.items():
            pq.put((-count, n))

        return [pq.get()[1] for _ in range(k)]


print(Solution().top_k_frequent([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5], 2))
