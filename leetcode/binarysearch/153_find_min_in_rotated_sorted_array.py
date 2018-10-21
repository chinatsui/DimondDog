class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]


print(Solution().findMin([3, 0, 1]))
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin([3, 4, 5, 1, 2]))
