def dfs(v):
    print(v,end=" ")
    for i in graph[v]:
        if not visitied[i]:
            visitied[i] = True
            dfs(i)

def bfs(v):
    from collections import deque
    queue = deque([v])

    while queue:
        v = queue.pop()
        print(v,end=" ")
        
        for i in graph[v]:
            if not visitied[i]:
                visitied[i] = True
                queue.appendleft(i)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visitied = [False]*(N+1)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visitied[V] = True
dfs(V)
print()

for i in range(N+1):
    visitied[i] = False

visitied[V] = True
bfs(V)