"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .

Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution:
    @staticmethod
    def find_order(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not numCourses:
            return []

        dg = DirectedGraph(numCourses)
        dg_dfs_order = DirectedGraphDFSOrder(dg)

        for pair in prerequisites:
            dg.add(pair[0], pair[1])

        if dg_dfs_order.has_cycle():
            return []
        else:
            return dg_dfs_order.order_list


class DirectedGraphDFSOrder:

    def __init__(self, g):
        self.cycle_found = False
        self.visited = set()
        self.on_stack = set()
        self.order_list = []

        for v in range(g.cnt):
            if v not in self.visited:
                self._dfs(g, v)

    def has_cycle(self):
        return self.cycle_found

    def _dfs(self, g, v):
        if self.cycle_found:
            return

        self.visited.add(v)
        self.on_stack.add(v)
        for w in g.adjacents[v]:
            if w not in self.visited:
                self._dfs(g, w)
            elif w in self.on_stack:
                self.cycle_found = True
                break
        self.on_stack.remove(v)
        self.order_list.append(v)

    def order(self):
        return list(reversed(self.order_list))


class DirectedGraph:

    def __init__(self, n):
        self.cnt = n
        self.adjacents = [set() for _ in range(n)]

    def add(self, v, w):
        adj_set = self.adjacents[v]
        if w not in adj_set:
            adj_set.add(w)


print(Solution().find_order(2, [[0, 1]]))
