class Solution:
    @staticmethod
    def three_sum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            m = i + 1
            n = len(nums) - 1
            while m < n:
                sum = nums[i] + nums[m] + nums[n]
                if sum < 0:
                    m += 1
                elif sum > 0:
                    n -= 1
                else:
                    res.append([nums[i], nums[m], nums[n]])
                    while m < n and nums[m] == nums[m + 1]:
                        m += 1
                    while m < n and nums[n] == nums[n - 1]:
                        n -= 1
                    m += 1
                    n -= 1
        return res


print(Solution().three_sum([-1, 0, 1, 2, -1, -4]))
print(Solution().three_sum([0, 0, 0, 0]))
