class Solution:
    @staticmethod
    def dailyTemperatures(T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0] * len(T)
        stack = []
        for (i, t) in enumerate(T):
            while stack and t > T[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
