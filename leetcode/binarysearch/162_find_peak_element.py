class Solution:
    @staticmethod
    def find_peak_element(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if mid == left:
                break

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left if nums[left] > nums[right] else right
