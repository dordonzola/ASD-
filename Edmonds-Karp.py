#O(V^2 *E)
from collections import deque

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.row

        queue = deque()

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()

            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def edmonds_karp(self, source, sink):

        parent = [-1] * self.row

        max_flow = 0

        while self.bfs(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


G=[[0,7,0,3,0,0,0],[0,0,0,4,6,0,0],[9,0,0,0,0,9,0],\
   [0,0,0,0,9,0,2],[0,0,0,0,0,0,0],[0,0,0,3,0,0,6],[0,0,0,0,8,0,0]]
d=Graph(G)
print(d.edmonds_karp(2,4))