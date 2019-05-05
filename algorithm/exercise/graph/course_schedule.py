"""
LeetCode-207

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution(object):

    @staticmethod
    def can_finish(num_courses, prerequisites):
        graph = DirectedGraph(num_courses)
        for pair in prerequisites:
            graph.add(pair[0], pair[1])
        check = DirectedGraphCycleCheck(graph)
        return not check.has_cycle


class DirectedGraphCycleCheck:

    def __init__(self, graph):
        self.has_cycle = False
        self.on_stack = set()
        self.visited = set()
        for i in range(graph.v_cnt):
            if i not in self.visited:
                self._dfs(graph, i)

    def _dfs(self, g, v):
        if self.has_cycle:
            return

        self.visited.add(v)
        self.on_stack.add(v)
        for w in g.adjacent[v]:
            if w not in self.visited:
                self._dfs(g, w)
            elif w in self.on_stack:
                self.has_cycle = True
                break
        self.on_stack.remove(v)


class DirectedGraph:

    def __init__(self, count):
        self.v_cnt = count
        self.adjacent = [set() for _ in range(count)]

    def add(self, v, w):
        v_adj = self.adjacent[v]
        if w not in v_adj:
            v_adj.add(w)


print(Solution().can_finish(2, [[1, 0]]))
