"""
LeetCode-210

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
    def find_order(num_courses, prerequisites):
        graph = DirectedGraph(num_courses)
        for pair in prerequisites:
            graph.add(pair[0], pair[1])
        check = DirectedGraphCheck(graph)
        return check.tsort if not check.cycle_found else []


class DirectedGraph:

    def __init__(self, count):
        self.v_cnt = count
        self.adj = [set() for _ in range(count)]

    def add(self, v, w):
        self.adj[v].add(w)


class DirectedGraphCheck:

    def __init__(self, graph):
        self.cycle_found = False
        self.visited = set()
        self.on_stack = set()
        self.tsort = []

        for v in range(graph.v_cnt):
            if v not in self.visited:
                self._dfs(graph, v)

    def _dfs(self, graph, v):
        if self.cycle_found:
            return

        self.visited.add(v)
        self.on_stack.add(v)
        for w in graph.adj[v]:
            if w not in self.visited:
                self._dfs(graph, w)
            elif w in self.on_stack:
                self.cycle_found = True
                return
        self.on_stack.remove(v)
        self.tsort.append(v)


print(Solution().find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
