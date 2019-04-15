"""
Given multiple time ranges: [l1, r1], [l2, r2], [l3, r3],
find the uncrossed time ranges at most between start_time and end_time.

Example:
Given: ranges = [6,8], [2,4], [3,5], [1,5], [5,9], [8,10], start_time = 1, end_time = 10
Result: [2,4], [6,8], [8,10]
"""


class Solution:

    @staticmethod
    def find_at_most(ranges, start, end):
        ranges = sorted(ranges, key=lambda r: r[0])
        res = [ranges[0]]

        for i in range(1, len(ranges)):
            p = res[-1]
            r = ranges[i]

            if r[0] < p[1] and r[1] < p[1]:
                res.pop()
                res.append(r)
            elif r[0] >= p[1]:
                res.append(r)

        return res


print(Solution().find_at_most([[6, 8], [2, 4], [3, 5], [1, 5], [5, 9], [8, 10]], 1, 10))
