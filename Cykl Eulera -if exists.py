#CZY ISTNIEJE cykl Eulera (jeśli jest ścieżka, zwraca path

def euler (graph):
    visited=[False]*len(graph)
    parent=[None]*len(graph)
    d=[0]*len(graph)
    odd=0

    def dfs_visit(u,i):
        nonlocal odd
        if not visited[u] and i!=0 and len(graph[u])!=0:
            return False
        visited[u]=True
        if len(graph[u])%2==1:
            odd+=1
        for v in graph[u]:
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                d[v]=d[u]+1
                if dfs_visit(v,i)==False:
                    return False

    dfs_visit(0, 0)
    old_odd=odd
    for i in range(1,len(graph)):
        odd=old_odd
        check=dfs_visit(i,i)
        if check==False:
            return False


    if odd==0:
        return True
    if odd==2:
        return "path"
    return False

G1=[[1,2],[0,2],[0,1,3,5],[2,4],[3,5],[2,4]]
G2=[[1,2],[0,2,3,5],[0,1,3,5],[1,2,4,5],[3,5],[1,2,3,4]]
G3=[[1],[0,4],[3,4,5,7],[2],[1,2,5,6,7,9],[2,4,10,11],[4,9],[2,4,9,11],[],[4,6,7,10],[5,9],[5,7]]
G4=[[1],[0,4],[3,4,5,7],[2],[1,2,5,6,7,9],[2,4,6,10,11],[4,5,9],[2,4,9,11],[],[4,6,7,10],[5,9],[5,7]]

print(euler(G1),euler(G2),euler(G3),euler(G4))



