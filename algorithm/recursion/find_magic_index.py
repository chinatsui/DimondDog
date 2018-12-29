"""
CC150-9.3
"""


class Solution:

    @staticmethod
    def find(nums):
        if not nums:
            return -1

        # lo, hi = 0, len(nums) - 1
        queue = [(0, len(nums) - 1)]
        # while lo < hi:
        while queue:
            (lo, hi) = queue.pop(0)
            mid = (lo + hi) // 2
            if nums[mid] == mid:
                return mid
            elif nums[mid] < mid:
                # hi = min(nums[mid], mid - 1)
                queue.append((lo, min(nums[mid], mid - 1)))
            else:
                # lo = max(nums[mid], mid + 1)
                queue.append((max(nums[mid], mid + 1), hi))
        return -1


t_nums = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(Solution().find(t_nums))
