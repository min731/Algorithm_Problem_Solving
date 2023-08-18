N, M, R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
order = [0 for _ in range(N+1)]

for _ in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for line in graph:
    line.sort()

stack = [R]
visited[R] = True

cnt = 1

while stack:

    v = stack.pop()
    # visited[v] =True

    if order[v]==0:
        order[v] = cnt
        cnt += 1

    for next in graph[v]:
        if not visited[next]:
            stack.append(next)
            visited[next] = True
for o in order[1:]:
    print(o)