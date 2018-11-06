class Solution:
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = nums[i] + nums[j]
                idx = self._binary_search(nums, j + 1, len(nums) - 1, -left)
                if 0 <= idx:
                    res.append([nums[i], nums[j], nums[idx]])
        return res

    @staticmethod
    def _binary_search(nums, lo, hi, target):
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if nums[lo] == target else -1


# print(sorted([-1, 0, 1, 2, -1, -4]))
print(Solution().three_sum([0, 0, 0, 0]))
