#O(ElogV) złożoność czasowa
from queue import PriorityQueue

def prim(G):
    n=len(G)
    inf=float("inf")
    d=[inf]*n
    visited=[[False for i in range(n)]for j in range(n)]
    d[0]=0
    parent=[None]*n
    Q=PriorityQueue()
    Q.put((d[0],0))

    while not Q.empty():
        u=Q.get()[1]
        for i in range(n):
            if not visited[u][i] and d[i]>G[u][i]:
                visited[u][i]=True
                visited[i][u]=True
                d[i]=G[u][i]
                parent[i]=u
                Q.put((d[i], i))

    child=[None]*n
    for i in range(n):
        if parent[i] is not None:
            child[parent[i]]=i

    result=[]
    i=0
    while i is not None:
        result.append(i)
        i=child[i]
    return result

inf=float("inf")

G = [[inf,5,inf,1,4],[5,inf,7,6,1],\
     [inf,7,inf,2,2],[1,6,2,inf,inf],[4,1,2,inf,inf]]

print(prim(G))
