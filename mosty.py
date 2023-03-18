# graf w postaci list sąsiedztwa

def bridge(G):
    inf=float("inf")
    n = len(G)
    visited = [False] * n
    parent = [-1] * n
    time = 0
    d = [-1] * n
    low = [inf] * n

    def dfs_visit(u, d):
        nonlocal  time

        d[u] = time
        low[u] = time
        time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(v, d)
            elif v != parent[u]:
                low[u] = min(d[u], d[v])

        if parent[u] != -1:
            low[parent[u]] = min(low[u], low[parent[u]])

    for i in range(n):
        if not visited[i]:
            dfs_visit(i, d)

    bridges = []
    for v in range(1, n):
        if d[v] == low[v]:
            bridges.append((v, parent[v]))

    return bridges

G1 = [[1, 3],[0, 2],[1, 3, 5],[0, 2, 4],[3],[2, 6, 7],[5, 7],[5, 6]]

G2 = [[1,8,7],[0,2,3],[1,3],[1,2],[5,6],[4,6],[4,5,7],[0,6,8],[0,7]]

print(bridge(G1),bridge(G2))