import time


class Solution1:
    def open_lock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        res = -1
        visited = set()

        start = '0000'
        q = [(start, 0)]
        while q:
            (cur, steps) = q.pop(0)

            if cur in visited or cur in deadends:
                continue

            if cur == target:
                res = steps if res == -1 else min(res, steps)

            visited.add(cur)
            for i in range(0, 4):
                q.append((self._move_up(cur, i), steps + 1))
                q.append((self._move_down(cur, i), steps + 1))
        return res

    @staticmethod
    def _move_up(cur, digit):
        val = (int(cur[digit]) + 1) % 10
        return cur[:digit] + str(val) + cur[digit + 1:]

    @staticmethod
    def _move_down(cur, digit):
        val = (int(cur[digit]) - 1) % 10
        return cur[:digit] + str(val) + cur[digit + 1:]


class Solution2:
    @staticmethod
    def open_lock(deadends, target):
        moved, q, cnt, move = set(deadends), ["0000"], 0, {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in
                                                           range(10)}
        if "0000" in moved:
            return -1
        while q:
            new = []
            cnt += 1
            for s in q:
                for i, c in enumerate(s):
                    for cur in (s[:i] + move[c][0] + s[i + 1:], s[:i] + move[c][1] + s[i + 1:]):
                        if cur not in moved:
                            if cur == target:
                                return cnt
                            new.append(cur)
                            moved.add(cur)
            q = new
        return -1


t_start = time.clock()
Solution1().open_lock(["2110", "0202", "1222", "2221", "1010"], '2010')
t_end = time.clock()
print(t_end - t_start)

t_start = time.clock()
Solution2().open_lock(["2110", "0202", "1222", "2221", "1010"], '2010')
t_end = time.clock()
print(t_end - t_start)
