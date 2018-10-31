class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        res = -1
        res_track = []
        visited = set()

        start = '0000'
        q = [(start, 0, [])]
        while q:
            item = q.pop(0)
            cur = item[0]
            step = item[1]
            track = item[2]

            if cur in visited:
                continue

            if cur in deadends:
                continue

            if cur == target:
                if res == -1:
                    res = step
                    res_track = track
                else:
                    res = min(res, step)
                    res_track = track + [target]

            visited.add(cur)
            for i in range(0, 4):
                move_up = self._move(cur, i, True)
                q.append((move_up, step + 1, track + [move_up]))
                move_down = self._move(cur, i, False)
                q.append((move_down, step + 1, track + [move_down]))
        res_track.insert(0, '0000')
        print(res_track)
        return res

    @staticmethod
    def _move(cur, digit, is_up):
        n_list = list(cur)
        n = int(n_list[digit])

        if is_up:
            n = n + 1 if n < 9 else 0
        else:
            n = n - 1 if n > 0 else 9

        n_list[digit] = n
        return ''.join(str(n) for n in n_list)


class Solution2:
    @staticmethod
    def openLock(deadends, target):
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


print(Solution().openLock(["2110", "0202", "1222", "2221", "1010"], '2010'))
