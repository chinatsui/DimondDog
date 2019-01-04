"""
LeetCode-742
"""
from collections import deque


class Solution1:
    def open_lock(self, deadends, target):
        """
        Usually BFS is a good way to find the shortest path to the goal.
        """
        if '0000' in deadends:
            return -1
            
        visited = set(deadends)
        
        start = '0000'
        q = deque()
        q.append((start, 1))
        visited.add(start)
        while q:
            (cur, steps) = q.popleft()
            for i in range(0, 4):
                up = self._move_up(cur, i)
                down = self._move_down(cur, i)

                if up not in visited:
                    if up == target:
                        return steps
                    q.append((up, steps + 1))
                    visited.add(up)

                if down not in visited:
                    if down == target:
                        return steps
                    q.append((down, steps + 1))
                    visited.add(down)
        return -1

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
        moved = set(deadends)
        q = ['0000']
        steps = 0
        move = {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}

        if '0000' in moved:
            return -1

        while q:
            next_round = []
            steps += 1
            for s in q:
                for i, c in enumerate(s):
                    for cur in (s[:i] + move[c][0] + s[i + 1:], s[:i] + move[c][1] + s[i + 1:]):
                        if cur not in moved:
                            if cur == target:
                                return steps
                            next_round.append(cur)
                            moved.add(cur)
            q = next_round

        return -1


print(Solution1().open_lock(["2110", "0202", "1222", "2221", "1010"], '2010'))
