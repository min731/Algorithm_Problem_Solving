N, M, R = map(int,input().split())
# print(N,M,R)

graph = {i+1:[] for i in range(N)}
print(graph)

for _ in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

print(graph)

stack = [R]
visited = [False for _ in range(N+1)]
visited[R] = True

while stack:

    v = stack.pop()
    print("v :",v)
    # [1,2,3]
    graph[v].sort()
    nexts = graph[v]

    for next in nexts:
        if not visited[next]:
            v1 = graph[v].pop()
            stack.append(v1)
            visited[v1] = True
    print("visited :",visited)