"""
LeetCode-300

Given an unsorted array of integers, find the length of longest increasing sub sequence.

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing sub sequence is [2,3,7,101], therefore the length is 4.

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    """
    The "tails" is an ArrayList storing the smallest "last element"
    of all increasing subsequences with the given length.

    For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:
    len = 1   :    [4], [5], [6], [3]        => min: 3, tails[0] = 3
    len = 2   :    [4,5], [4,6], [5,6]       => min: 5, tails[1] = 5
    len = 3   :    [4,5,6]                   => min: 6, tails[2] = 6
    And, we can easily prove that the "tails" is an increasing ArrayList also.

    For each time we access the number in nums, we just binary search it in tails,
    if it is larger than any existent tail, then append it to the tails,
    otherwise we update it in the corresponding position.

    Finally, the size of tails is the length of the longest increasing subsequence.
    (This is indeed hard to be thought of, but it surely is.)
    """

    def len_of_lis(self, nums):
        if not nums:
            return 0

        tails = []
        for n in nums:
            idx = self._binary_search(tails, n)
            if idx == len(tails):
                tails.append(n)
            else:
                tails[idx] = n
        return len(tails)

    @staticmethod
    def _binary_search(tails, n):
        if not tails:
            return 0

        lo, hi = 0, len(tails) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            val = tails[mid]

            if val == n:
                return mid
            elif val < n:
                lo = mid + 1
            else:
                hi = mid

        return lo if n <= tails[lo] else lo + 1


print(Solution().len_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
