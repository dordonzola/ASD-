#O(V+E) -Time complexity
#Changes Adjacency List to adjacency matrix
#When there is Euler's cycle it works well, if there's no it doesn't work (!)


def change(G):
    maxi=0
    for i in range(len(G)):
        if G[i][1]>maxi:
            maxi=G[i][1]
    G2=[[0 for i in range(maxi+1)]for j in range(maxi+1)]
    for i in range(len(G)):
        for j in (G[i]):
            G2[i][j]=1
    return G2

def dfs_visit(u,result,G):
    for j in range(len(G[u])) :
        if G[u][j]!=0:
            G[u][j]=0
            G[j][u]=0
            dfs_visit(j,result,G)
            result.append(j)


def euler(G):
    G=change(G)
    result=[]
    dfs_visit(0,result,G)

    return result





G1=[[1,2],[0,2],[0,1,3,5],[2,4],[3,5],[2,4]]
G2=[[1,2],[0,2,3,5],[0,1,3,5],[1,2,4,5],[3,5],[1,2,3,4]]


print(euler(G1),euler(G2))


