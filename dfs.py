#graf w postaci list sąsiedztwa

# O(|V|+|E|)
#O(h) h-długość najdłuższej prostej ścieżki -pamięciowa

def dfs (graph,s):
    visited=[False]*len(graph)
    parent=[None]*len(graph)
    d=[0]*len(graph)

    def dfs_visit(u):
        visited[u]=True
        for v in graph[u]:
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                d[v]=d[u]+1
                dfs_visit(v)


    dfs_visit(s)
    return d

T=[[1],[0,5],[5],[4],[3,5],[1,2,4]]

print(dfs(T,0))


