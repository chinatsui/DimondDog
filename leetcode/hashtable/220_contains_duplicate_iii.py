class Solution:

    @staticmethod
    def contains_nearby_almost_duplicate(nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False

        d = {}
        w = t + 1
        for (i, n) in enumerate(nums):
            m = n // w

            if m in d:
                return True

            if m - 1 in d and abs(n - d[m - 1]) < w:
                return True

            if m + 1 in d and abs(n - d[m + 1]) < w:
                return True

            d[m] = n

            if i >= k:
                del d[nums[i - k] // w]
        return False


print(Solution().contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], k=2, t=3))
