N, M, V = map(int, input().split())

graph = []
visited = []

for _ in range(N+1):
    graph.append([])
    visited.append(False)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

# dfs
visited[V] = True

def dfs(v):
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
dfs(V)

print()
# bfs
visited = []
for _ in range(N+1):
    visited.append(False)
visited[V] = True

from collections import deque
queue = deque([V])

while queue:
    v = queue.pop()
    print(v,end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            queue.appendleft(i)