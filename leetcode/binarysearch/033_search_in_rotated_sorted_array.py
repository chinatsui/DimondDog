class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot = self.find_pivot(nums)
        lo = 0
        hi = len(nums) - 1

        if nums[pivot] <= target <= nums[hi]:
            return self.binary_search(nums, pivot, hi, target)
        elif lo <= pivot - 1:
            return self.binary_search(nums, lo, pivot, target)
        else:
            return -1

    @staticmethod
    def find_pivot(nums):
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    @staticmethod
    def binary_search(nums, lo, hi, target):
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


t_res = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print(t_res)
