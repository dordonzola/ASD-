#O(ElogV) -czasowa
#O(E + VlogV) - pamięciowa

from queue import PriorityQueue
def relax (G,d,parent,u,v):
    if d[v]>(d[u]+G[u][v]):
        d[v]=d[u]+G[u][v]
        parent[v]=u

def dijkstra(G,s):
    n = len(G)
    visited=[False]*n

    inf = float("inf")
    d = [inf] * n
    d[s] = 0
    parent = [None] * n
    Q = PriorityQueue()
    Q.put((d[s], s))

    while not Q.empty():
        u = Q.get()[1]
        if not visited[u]:
            visited[u]=True
            for i in range(n):
                if G[u][i]!=0:
                    relax(G, d, parent, u, i)
                Q.put((d[i], i))

    return d

G= [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]


print(dijkstra(G,0))