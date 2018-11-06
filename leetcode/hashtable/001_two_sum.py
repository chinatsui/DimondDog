class Solution:
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict()
        for (i, n) in enumerate(nums):
            if n in mapping:
                return [i, mapping[n]]
            else:
                mapping[target - n] = i
        return []
