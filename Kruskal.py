#O(ElogV) - złożoność
class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(E,n):
    E.sort()
    V = [Node(i) for i in range(n)]
    A=[]
    for e in E:
        u=e[1]
        v=e[2]
        if find(V[u]) != find(V[v]):
            A.append(e)
            union(V[u],V[v])
    return A

n=6
E=[(1,0,1),(7,0,5),(8,1,5),(4,1,3),(12,1,2),(3,2,5),(6,2,3),(5,3,4),(2,4,5)]#waga i dwa wierzchołki
#   (1,1,0),(7,5,0),(8,5,1),(4,3,1),(12,2,1),(3,5,2),(6,3,2),(5,4,3),(2,5,4)]

print(Kruskal(E,n))