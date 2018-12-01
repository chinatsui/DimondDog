"""
For convenience, we use array 'arr' to store a graph.
The index 'i' represents the vertex, and 'arr[i]' represents its adjacent vertexes.
"""
from collections import deque


class Graph:

    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = [set() for _ in range(v)]

    def V(self):
        return self.V

    def E(self):
        return self.E

    def add(self, v, w):
        if w in self.adj[v]:
            return

        if v in self.adj[w]:
            return

        self.E += 1
        self.adj[v].add(w)
        self.adj[v].add(w)

    def adj(self, v):
        return self.adj[v]


class GraphDfsPath:

    def __init__(self, g, s):
        self.s = s
        self.visited = set()
        self.edge_to = [i for i in range(g.V())]
        self._dfs(g, s)

    def _dfs(self, g, v):
        self.visited.add(v)
        for w in g.adj(v):
            if w not in self.visited:
                self.edge_to[w] = v
                self._dfs(g, w)

    def has_path_to(self, v):
        return v in self.visited

    def path_to(self, v):
        path = [v]
        while v != self.s:
            w = self.edge_to[v]
            path.append(w)
            v = w
        return path


class GraphBfsPath:

    def __init__(self, g, s):
        self.s = s
        self.visited = set()
        self.edge_to = [i for i in range(g.V())]
        self.bfs(g, s)

    def _bfs(self, g, v):
        q = deque()
        q.append(v)
        while q:
            v = q.popleft()
            self.visited.add(v)
            for w in g.adj(v):
                if w not in self.visited:
                    self.edge_to[w] = v
                    q.append(w)

    def has_path_to(self, v):
        return v in self.visited

    def path_to(self, v):
        path = [v]
        while v != self.s:
            w = self.edge_to[v]
            path.append(w)
            v = w
        return path


class ConnectedComponent:

    def __init__(self, g):
        self.visited = set()
        self.ids = [0] * g.V()
        self.count = 0
        for v in range(g.V()):
            if v not in self.visited:
                self._dfs(g, v)
                self.count += 1

    def _dfs(self, g, v):
        self.visited.add(v)
        self.ids[v] = self.count
        for w in g.adj(v):
            if w not in self.visited:
                self._dfs(g, w)

    def connected(self, v, w):
        return self.ids[v] == self.ids[w]

    def count(self):
        return self.count

    def id(self, v):  # get the id of a component in which the vertex exists in
        return self.ids[v]


class DirectedGraph(Graph):

    def add(self, v, w):
        if w in self.adj(v):
            return

        self.adj(v).add(w)
        self.E += 1

    def reverse(self):
        res = DirectedGraph(self.V)
        for v in range(self.V):
            for w in self.adj(v):
                res.add(w, v)
        return res


class DirectedGraphCycleCheck:

    def __init__(self, g):
        self.visited = set()
        self.on_stack = set()
        self.cycle = None
        self.edge_to = [i for i in range(g.V())]

    def _dfs(self, g, v):
        self.visited.add(v)
        self.on_stack.add(v)
        for w in g.adj(v):
            if self.has_cycle():
                return

            if w not in self.visited:
                self.edge_to[w] = v
                self._dfs(g, w)
            elif w in self.on_stack:
                self.cycle = [v]
                while v != w:
                    k = self.edge_to[v]
                    self.cycle.append(k)
        self.on_stack.remove(v)

    def has_cycle(self):
        return self.cycle is not None

    def cycle(self):
        return self.cycle


class DirectedGraphDFSOrder:

    def __init__(self, g):
        self.pre = deque()
        self.post = deque()
        self.reverse_post = []  # topological order
        self.visited = set()
        for v in g.V():
            if v not in self.visited:
                self._dfs(g, v)

    def _dfs(self, g, v):
        self.visited.add(v)
        self.pre.appendleft(v)
        for w in g.adj(v):
            if w not in self.visited:
                self._dfs(g, w)
        self.post.appendleft(v)
        self.reverse_post.append(v)

    def pre(self):
        return self.pre

    def post(self):
        return self.post

    def reverse_post(self):
        return self.reverse_post


class TopologicalSort:

    def __init__(self, g):
        self.order = None
        self.cycle_check = DirectedGraphCycleCheck(g)
        if not self.cycle_check.has_cycle():
            self.order = DirectedGraphDFSOrder(g).reverse_post()

    def order(self):
        return self.order()

    def is_dag(self):
        return self.order() is not None
