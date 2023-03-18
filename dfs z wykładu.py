#listy sąsiedztwa
#zwraca None

# O(|V|+|E|)
#O(h) h-długość najdłuższej prostej ścieżki -pamięciowa

def dfs(G):
    visited = [False for i in range(len(G))]
    parent = [None for i in range(len(G))]
    time=0


    def dfs_visit(G,u):
        nonlocal time
        time+=1
        if time==len(G):
            if G[u][0]==0:
                return
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                dfs_visit(G,v)



    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(G,u)





G2=[[3,4,5],[2,3,5],[1,3,5],[0,1,2,4],[0,3],[0,1,2]]
T=[[1,5],[0,2,4,5],[1,3,5],[2,4],[1,3,5],[0,1,2,4]]

print(dfs(T))