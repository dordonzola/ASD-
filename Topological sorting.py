#O(V+E)

def top_sort(G):
    visited=[False]*len(G)
    rev_sorted=[]

    def dfs_visit(u,st):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v,st)
        st.append(u)

    for i in range (len(G)):
        if not visited[i]:
            dfs_visit(i,rev_sorted)

    sorted=[]
    for i in range(len(rev_sorted)-1,-1,-1):
        sorted.append(rev_sorted[i])

    return sorted


G=[[1,5],[2],[],[4],[],[3],[0],[6],[7]]

print(top_sort(G))



