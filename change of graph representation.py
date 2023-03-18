'''from this:
[[0,1,0],\
 [1,0,1],\
 [0,1,0]]

to that:
[1],[0,2],[1]'''

n1=len(G1)
    G=[[]for i in range(n1)]
    for i in range(n1):
        for j in range(n1):
            if G1[i][j]==1:
                G[i].append(j)
