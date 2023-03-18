 #O(V^3) - czasowa
 #O(V^2) - pamięciowa

def floyd(T):
    n=len(T)
    inf=float("inf")
    D=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j: D[i][j]=0
            else: D[i][j]=T[i][j]


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j]>D[i][k]+D[k][j]:
                    D[i][j]=D[i][k]+D[k][j]

    return D

inf=float("inf")
T=[[0,5,4,8,inf],[-4,0,-2,inf,5],[inf,inf,0,5,2],[-1,2,inf,0,-1],[inf,inf,4,2,0]]
print(floyd(T))
