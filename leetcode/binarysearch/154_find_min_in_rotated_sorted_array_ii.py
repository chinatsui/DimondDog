class Solution:
    @staticmethod
    def find_min(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] == nums[hi]:
                hi -= 1
            else:
                lo = mid + 1
        return nums[lo]


print(Solution().find_min([2, 2, 2, 0, 1]))
