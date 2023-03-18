#O(V^3) - czasowa (ten program, moze byc dla innego programu VE)
#O(V) - pamięciowa

def relax (G,d,parent,u,v):
    if d[v]>(d[u]+G[u][v]):
        d[v]=d[u]+G[u][v]
        parent[v]=u

def bellman_ford(G,s):
    n=len(G)
    inf=float("inf")
    d=[inf]*n
    parent=[None]*n
    d[s]=0
    for i in range(n-1):
        for x in range(n):
            for y in range(n):
                if G[x][y]!=inf: relax(G,d,parent,x,y)
    #print(d)
    for i in range(n):
        for j in range(n):
            if d[j]>d[i]+G[i][j]:
                return False

    return d

inf=float("inf")
G=[[inf,-5,-1,inf,inf],[inf,inf,inf,4,inf],\
   [inf,inf,inf,8,inf],[inf,inf,inf,inf,1],[10,inf,inf,inf,inf]]

print(bellman_ford(G,0))