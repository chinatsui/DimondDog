class Solution:
    @staticmethod
    def contains_nearby_duplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        diff = len(nums)
        num_idx_map = dict()

        for (i, n) in enumerate(nums):
            if n in num_idx_map:
                diff = min(diff, i - num_idx_map[n])
                if diff <= k:
                    return True
                num_idx_map[n] = i
            else:
                num_idx_map[n] = i
        return False
