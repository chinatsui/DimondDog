class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        cache = dict()
        res = []

        for n in range(num + 1):
            cnt = 0
            x = n
            while n > 0:
                cnt += n % 2
                n //= 2
                if n in cache:
                    cnt += cache[n]
                    break
            cache[x] = cnt
            res.append(cnt)
        return res


print(Solution().countBits(2))
