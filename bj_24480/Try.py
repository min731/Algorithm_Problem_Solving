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
visited = [False for _ in range(N)]
visited[R-1] = True

while stack:

    v = stack.pop()
    print("v :",v)
    # [1,2,3]
    nexts = graph[v]
    nexts.sort()
    print("nexts : ",nexts)

    for next in nexts:
        if not visited[next]:
            stack.append(next)
            visited[next] = True