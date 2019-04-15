"""
Given a number n, remove k digits to make the number smallest.

Example 1:
Give: 53429, 2
Remove: 5, 4, then return 329
"""


class Solution:

    @staticmethod
    def remove_k_digits(n, k):
        if not k:
            return

        nums = list(map(int, str(n)))
        while k > 0:
            for i in range(0, len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums = nums[:i] + nums[i + 1:]
                    break
                elif i == len(nums) - 2:
                    nums = nums[:i + 1]
            k -= 1

        return int(''.join(list(map(str, nums))))


print(Solution().remove_k_digits(53429, 2))
print(Solution().remove_k_digits(12345, 2))
print(Solution().remove_k_digits(4556847594546, 5))
