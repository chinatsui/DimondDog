"""
LeetCode-239

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""


class Solution:
    @staticmethod
    def max_sliding_window(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k:
            return []

        res = []
        n = len(nums)
        cache = []
        for i in range(0, n - k + 1):
            idx, max_val = i, nums[i]

            if cache:
                (last_idx, last_max_val) = cache.pop(0)
                if last_idx >= i:
                    idx = last_idx
                    max_val = last_max_val

            for j in range(idx + 1, i + k):
                if nums[j] > max_val:
                    idx = j
                    max_val = nums[j]
            res.append(max_val)
            cache.append((idx, max_val))
        return res


print(Solution().max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
