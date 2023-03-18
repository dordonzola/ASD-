#listy sąsiedztwa
#zwraca odległości

# O(|V|+|E|) czasowa i pamięciowa

from queue import Queue

def bfs(graph, s):
     queue=Queue()
     visited=[False]*len(graph)
     parent=[None]*len(graph)
     d=[0]*len(graph)

     queue.put(s)
     visited[s]=True

     while not queue.empty():
         u=queue.get()
         for v in graph[u]:
             if not visited[v]:
                 visited[v]=True
                 d[v]=d[u]+1
                 parent[v]=u
                 queue.put(v)

     return d



T=[[1,5],[0,2,4,5],[1,3,5],[2,4],[1,3,5],[0,1,2,4]]

print(bfs(T,0))