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
order = [-1]

while stack:

    v = stack.pop()
    order.append(v)
    print(v)
    graph[v].sort()
    nexts = graph[v]
    print("nexts : ",nexts)

    # [4,2]
    for next in nexts:
        if not visited[next]:
            stack.append(next)
            visited[next] = True
    print("stack :",stack)

print("order : ",order)
for i in range(1,N+1):
    try:
        print(order.index(i))
    except:
        print(0)