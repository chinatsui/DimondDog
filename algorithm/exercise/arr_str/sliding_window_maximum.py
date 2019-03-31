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
from collections import deque


class Solution:
    @staticmethod
    def max_sliding_window(nums, k):
        """
        Use a doubly queue to store the idx, each time we do the following things:
        1) If deq is not empty, do while loop to check if most left idx is out of sliding window, if yes, pop it.
        2) If deq is not empty, do While loop to check if the number of most right idx < nums[i], if yes, pop it.
        3) Append i into deque.
        4) After 1) and 2), add the number of current most left idx in deque to res for the current sliding window.
        """
        if not nums or not k:
            return []

        res, deq = [], deque()
        for i in range(len(nums)):
            while deq and deq[0] < i - k + 1:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            if i >= k - 1:
                idx = deq[0]
                res.append(nums[idx])

        return res


print(Solution().max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
