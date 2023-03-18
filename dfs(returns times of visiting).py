#adjacency lists


# O(|V|+|E|) -time complexity
#O(h) h-length of the longest path

def dfs(G):
    visited = [False]*len(G)
    parent = [None]*len(G)
    czas=[0 for i in range(len(G))]


    time = 1
    def dfs_visit(u):
        nonlocal time

        visited[u] = True
        czas[u]=time
        time += 1
        for v in G[u]:
            if visited[v] == False:
                parent[v] = u
                dfs_visit(v)


    dfs_visit(0)
    return czas

G = [
    [1, 4],
    [0, 2],
    [1, 3],
    [5, 2],
    [5, 0],
    [3, 4]
]
print(dfs(G))
