"""
LeetCode-621

Given a char array representing tasks CPU need to do.
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order.
Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

from collections import Counter
from queue import PriorityQueue


class Task(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __lt__(self, other):
        return self.count > other.countast


class Solution2(object):
    """
    AAAAABBBEEFFGG 3
    Do stats we can get: A(5), B(3), E(2), F(2), G(2)
    The final task execution plan could be (AXXX) + (AXXX) + (AXXX) + (AXXX) + A, then insert others into those groups,
    therefore we can get below result:
       (n + 1) & (most_freq - 1) + count of most_freq, that is:
       (3 + 1) * (5 - 1) + 1 = 17
    However, sometimes by following above pattern, we might NOT have enough space to insert all other tasks, e.g:
    AACCCBEEE 2 -> (CEX) + (CEX) + CE + X, actually the result in this situation must be the len(tasks).
    """

    @staticmethod
    def least_interval(tasks, n):
        freq_list = [_ for _ in Counter(tasks).values()]
        most_freq = max(freq_list)
        most_freq_cnt = freq_list.count(most_freq)
        return max(len(tasks), (n + 1) * (most_freq - 1) + most_freq_cnt)


class Solution(object):
    def least_interval(self, tasks, n):
        if not n:
            return len(tasks)

        pq = PriorityQueue()
        for item in Counter(tasks).items():
            pq.put(Task(item[0], item[1]))

        cooling_list = [None for _ in range(n + 1)]

        res = 0
        while not self._is_finished(pq, cooling_list):
            res += 1
            if not pq.empty():
                task = pq.get()
                task.count -= 1
                self._reduce_all(pq, cooling_list)
                if task.count:
                    cooling_list[n] = task
            else:
                self._reduce_all(pq, cooling_list)
        return res

    @staticmethod
    def _is_finished(pq, cooling_list):
        if not pq.empty():
            return False

        for t in cooling_list:
            if t:
                return False

        return True

    @staticmethod
    def _reduce_all(pq, cooling_list):
        for i in range(len(cooling_list) - 1):
            if i == 0 and cooling_list[1]:
                pq.put(cooling_list[1])
            else:
                cooling_list[i] = cooling_list[i + 1]
            cooling_list[i + 1] = None


print(Solution2().least_interval([ch for ch in 'AAABBB'], 0))
print(Solution2().least_interval([ch for ch in 'ABCAB'], 2))
print(Solution2().least_interval([ch for ch in 'AAABBB'], 2))
print(Solution2().least_interval([ch for ch in 'AAAAABBBEEFFGG'], 3))
