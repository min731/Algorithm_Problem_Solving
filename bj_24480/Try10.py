N, M, R = map(int,input().split())
# print(N,M,R)

graph = {i+1:[] for i in range(N)}
print(graph)

for _ in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for k in graph.keys():
    graph[k].sort()

print(graph)

stack = [R]
visited = [False for _ in range(N+1)]
visited[R] = True
print("----------------")
order = [0 for _ in range(N+1)]
cnt = 1

while stack:

    v = stack.pop()

    if order[v]==0:
        order[v] = cnt
        cnt += 1
    print(v)

    # [4,2]
    for next in graph[v]:
        if not visited[next]:
            stack.append(next)
            visited[next] = True
    print("stack :",stack)

print("order : ",order)
for o in order[1:]:
    print(o)