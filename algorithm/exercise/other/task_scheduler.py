from collections import Counter
import heapq


class Solution(object):
    def least_interval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not n:
            return len(tasks)

        counter = Counter(tasks)
        cooling = {i: set() for i in range(1, n + 1)}
        # cooling[0] = set([task for task, cnt in counter.items()])
        cooling[0] = []
        cooling[0] = [heapq.heappush(cooling[0], (task, cnt)) for (task, cnt) in counter.items()]

        res = 0
        while counter:
            res += 1
            if cooling[0]:
                task = self._retrieve(cooling[0], counter)
                counter[task] -= 1
                self._reduce_all(cooling)
                if counter[task] == 0:
                    del counter[task]
                else:
                    cooling[n].add(task)
            else:
                self._reduce_all(cooling)
        return res

    @staticmethod
    def _reduce_all(cooling):
        for i in range(len(cooling) - 1):
            cooling[i] |= cooling[i + 1]
            cooling[i + 1].clear()

    @staticmethod
    def _retrieve(cool_0_set, counter):
        task, cnt = None, 0
        for t in cool_0_set:
            if counter[t] > cnt:
                cnt = counter[t]
                task = t
        cool_0_set.remove(task)
        return task
        # entries = sorted(counter.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        # for e in entries:
        #     if e[0] in cool_0_set:
        #         cool_0_set.remove(e[0])
        #         return e[0]


print(Solution().least_interval(["A", "B", "C", "A", "B"], 2))
# print(Solution().least_interval(["A", "A", "A", "B", "B", "B"], 2))
