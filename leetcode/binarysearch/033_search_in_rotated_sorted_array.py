class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2

            if nums[lo] <= nums[mid]:
                # lo...mid is sorted
                if nums[lo] <= target <= nums[mid]:
                    return self._binary_search(nums, lo, mid, target)
                else:
                    lo = mid + 1
            else:
                # mid...hi is sorted
                if nums[mid] <= target <= nums[hi]:
                    return self._binary_search(nums, mid, hi, target)
                else:
                    hi = mid
        return lo if nums[lo] == target else -1

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


t_res = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print(t_res)
