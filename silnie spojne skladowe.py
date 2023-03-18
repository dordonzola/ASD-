
def reverse(G):
    N=len(G)
    new_G=[[] for _ in range(N)]
    for i in range(N):
        for j in G[i]:
            new_G[j].append(i)

    return new_G

#funkcja zwraca indexy pojedynczych elementów ze spójnych składowych bo mi się już nie chciało
#O(V+E)

def dfs (G,order):
    sss=[]
    N=len(G)
    visited=[False]*N
    process_time=[-1]*N
    time=1

    def dfs_visit(u,process_time,part,i):
        nonlocal time
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                part.append(v)
                dfs_visit(v,process_time,part,i)

        process_time[u]=time,u
        time+=1
    if not order:
        for s in range (N):
            if not visited[s]:
                dfs_visit(s,process_time,[],0)
    else:
        i=0

        for s in range(N):
            part=[]
            if not visited[order[s][1]]:
                part.append(order[s][1])
                dfs_visit(order[s][1],process_time,part,i)
                i+=1
                sss.append(part)
    return process_time , sss

def SSS(G):
    process_time=dfs(G,None)[0]
    process_time=sorted(process_time)
    sss=dfs(G,process_time)[1]

    return sss

G=[[1],[2,3],[0,7],[4,6],[5],[3],[5],[10],[6,7],[8,5],[9]]
print(SSS(G))