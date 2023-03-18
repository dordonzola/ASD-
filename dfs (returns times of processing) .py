#Adjacency list


# O(|V|+|E|)
#O(h) h-length of longest path

def dfs(G):
    visited = [None]*len(G)
    parent = [None]*len(G)
    czas=[0 for i in range(len(G))]
    for i in range(len(G)):
        visited[i] = False

    time = 1
    def dfs_visit(u):
        nonlocal G, czas, time, visited, parent

        visited[u] = True

        for v in G[u]:
            if visited[v] == False:
                parent[v] = u
                dfs_visit(v)

        czas[u] = time
        time += 1

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
