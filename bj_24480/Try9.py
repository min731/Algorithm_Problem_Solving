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
print("----------------")
order = [0 for _ in range(N+1)]
cnt = 1

while stack:

    v = stack.pop()
    order[v] = cnt
    print(v)
    graph[v].sort()

    # [4,2]
    for next in graph[v]:
        if not visited[next]:
            stack.append(next)
            visited[next] = True
            
    print("stack :",stack)
    cnt += 1

print("order : ",order)
for i in range(1,len(order)):
    print(order[i])