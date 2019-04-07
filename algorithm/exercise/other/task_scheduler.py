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

    @staticmethod
    def least_interval(tasks, n):
        c = [0 for _ in range(26)]
        for ch in tasks:
            c[ord(ch) - ord('A')] += 1

        c = sorted(c)
        i = 25
        while i >= 0 and c[i] == c[25]:
            i -= 1

        return max(len(tasks), (c[25] - 1) * (n + 1) + 25 - i)


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


# print(Solution().least_interval(["A", "B", "C", "A", "B"], 2))
print(Solution2().least_interval(["A", "A", "A", "B", "B", "B"], 2))
