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
