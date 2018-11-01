class Solution:
    def num_squares(self, n):
        squares = self._squares(n);
        cnt = 0
        remains = {n}
        while remains:
            cnt += 1
            tmp = set()
            for remain in remains:
                for sq in squares:
                    if remain < sq:
                        break
                    elif remain == sq:
                        return cnt
                    else:
                        tmp.add(remain - sq)
            remains = tmp

    @staticmethod
    def _squares(n):
        i = 1
        squares = []
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1
        return squares


print(Solution().num_squares(1))
