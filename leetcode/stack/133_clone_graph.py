# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        res = UndirectedGraphNode(node.label)
        visited = set()
        mapping = {}
        self._dfs(res, node, mapping, visited)
        return res

    def _dfs(self, copy, origin, mapping, visited):
        if origin in visited:
            return

        visited.add(origin)
        for n in origin.neighbors:
            copy_neighbor = None
            if n in mapping:
                copy_neighbor = mapping[n]
            else:
                copy_neighbor = UndirectedGraphNode(n.label)
                mapping[n] = copy_neighbor
            copy.neighbors.append(copy_neighbor)
            self._dfs(copy_neighbor, n, mapping, visited)
