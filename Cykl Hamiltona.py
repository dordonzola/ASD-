#Graf ważony
#O(n!)
def hamilton(G):
    n = len(G)
    visited = [False for i in range(n)]
    stack = []

    def dfs_visit(G, u):
        nonlocal  stack
        stack.append(u)
        if len(stack) == n:
            if G[u][0] == 0:
                return stack
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                result = dfs_visit(G, v)
                if result is not None:
                    return result
        visited[u] = False
        stack.pop()

    dfs_visit(G, 0)
    return stack


# G = [ [[1],[2,3,4]],
# [[0],[2,5,6]],
# [[1,5,6],[0,3,4]],
# [[0,2,4],[5,7,8]],
# [[0,2,3],[6,7,9]],
# [[1,2,6],[3,7,8]],
# [[1,2,5],[4,7,9]],
# [[4,6,9],[3,5,8]],
# [[3,5,7],[9]],
# [[4,6,7],[8]] ]
#
# print(droga(G))
# runtests(droga, all_tests=True)
# G1=[[1,4,5],[1,2,5],[1,3],[2,4],[0,3,5],[0,1,4]]
G2 = [[3, 4, 5], [2, 3, 5], [1, 3, 5], [0, 1, 2, 4], [0, 3], [0, 1, 2]]
print(hamilton(G2))