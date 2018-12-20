"""
CC150-9.3
"""


class Solution:

    @staticmethod
    def find(nums):
        if not nums:
            return -1

        queue = [(0, len(nums) - 1)]
        while queue:
            lo, hi = queue.pop()
            mid = (lo + hi) // 2
            if nums[mid] == mid:
                return mid
            elif nums[mid] < mid:
                queue.append((lo, min(nums[mid], mid - 1)))
            else:
                queue.append((max(nums[mid], mid + 1), hi))
        return -1


t_nums = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(Solution().find(t_nums))
